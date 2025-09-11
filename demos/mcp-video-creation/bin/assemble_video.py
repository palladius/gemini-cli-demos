#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video Assembler Script

This script reads a YAML file that defines a video structure (scenes, audio, etc.)
and uses ffmpeg to assemble the final video.

Usage:
    python3 bin/assemble_video.py /path/to/your/video_plan.yaml
"""

import argparse
import os
import subprocess
import sys
import tempfile
import yaml
from pathlib import Path

def run_ffmpeg_command(command):
    """Runs an ffmpeg command, checks for errors, and prints output."""
    print(f"🚀 Executing: {' '.join(command)}")
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print("❌ FFMPEG Error:")
        print(stderr)
        sys.exit(1)
    print("✅ Success")
    return stdout

def assemble_video(plan_path):
    """Main function to assemble the video based on the YAML plan."""
    
    # Get absolute path of the plan file
    plan_path = Path(plan_path).resolve()
    
    # The working directory should be the directory containing the plan file
    work_dir = plan_path.parent
    os.chdir(work_dir)
    print(f"📂 Working directory set to: {work_dir}")

    with open(plan_path, 'r') as f:
        plan = yaml.safe_load(f)

    print(f"🎬 Starting video assembly for: {plan['title']}")

    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"🛠️ Created temporary directory: {temp_dir}")
        
        processed_scene_files = []
        
        for i, scene in enumerate(plan['scenes']):
            scene_num = scene['scene']
            print(f"\nProcessing Scene {scene_num}: {scene.get('description', '')}")
            
            scene_video = Path(scene['video'])
            if not scene_video.exists():
                print(f"🚨 Error: Video file not found: {scene_video}")
                sys.exit(1)

            # --- Audio Processing ---
            music_track = scene.get('music')
            narration_track = scene.get('narration')
            final_audio_for_scene = None
            
            # 1. Prepare Narration
            processed_narration = None
            if narration_track:
                narration_file = Path(narration_track['source'])
                processed_narration = Path(temp_dir) / f"scene_{scene_num}_narration.wav"
                cmd = [
                    'ffmpeg', '-i', str(narration_file),
                    '-ss', str(narration_track.get('start_time', 0)),
                    '-to', str(narration_track.get('end_time', 999)),
                    '-y', str(processed_narration)
                ]
                run_ffmpeg_command(cmd)

            # 2. Prepare Music
            processed_music = None
            if music_track:
                music_file = Path(music_track['source'])
                processed_music = Path(temp_dir) / f"scene_{scene_num}_music.wav"
                volume = music_track.get('volume_db', plan.get('settings', {}).get('music_volume_db', 0))
                cmd = [
                    'ffmpeg', '-i', str(music_file),
                    '-filter:a', f"volume={volume}dB",
                    '-y', str(processed_music)
                ]
                run_ffmpeg_command(cmd)

            # 3. Combine Audio
            if processed_narration and processed_music:
                final_audio_for_scene = Path(temp_dir) / f"scene_{scene_num}_final_audio.wav"
                cmd = [
                    'ffmpeg',
                    '-i', str(processed_narration),
                    '-i', str(processed_music),
                    '-filter_complex', 'amix=inputs=2:duration=longest',
                    '-y', str(final_audio_for_scene)
                ]
                run_ffmpeg_command(cmd)
            elif processed_narration:
                final_audio_for_scene = processed_narration
            elif processed_music:
                final_audio_for_scene = processed_music

            # --- Video and Audio Juxtaposition ---
            output_scene_video = Path(temp_dir) / f"scene_{scene_num}_processed.mp4"
            
            if final_audio_for_scene:
                # If we have custom audio, replace the video's audio with it
                cmd = [
                    'ffmpeg',
                    '-i', str(scene_video),
                    '-i', str(final_audio_for_scene),
                    '-c:v', 'copy', # Copy video stream without re-encoding
                    '-c:a', 'aac',   # Re-encode audio to aac
                    '-map', '0:v:0', # Map video from first input
                    '-map', '1:a:0', # Map audio from second input
                    '-shortest',     # Finish encoding when the shortest input stream ends
                    '-y', str(output_scene_video)
                ]
                run_ffmpeg_command(cmd)
            else:
                # If no custom audio, just copy the original video
                print("ℹ️ No custom audio for this scene. Using original video.")
                # We still copy it to the temp dir to have a consistent list
                output_scene_video = scene_video.copy(output_scene_video)


            processed_scene_files.append(output_scene_video)

        # --- Final Concatenation ---
        print("\n🎞️ Concatenating all processed scenes...")
        concat_list_path = Path(temp_dir) / "concat_list.txt"
        with open(concat_list_path, 'w') as f:
            for video_file in processed_scene_files:
                f.write(f"file '{video_file.resolve()}'\n")
        
        output_filename = Path(plan['output_filename'])
        cmd = [
            'ffmpeg',
            '-f', 'concat',
            '-safe', '0',
            '-i', str(concat_list_path),
            '-c', 'copy', # Copy streams without re-encoding
            '-y', str(output_filename)
        ]
        run_ffmpeg_command(cmd)
        
        print(f"\n🎉 Video assembly complete! Output file: {output_filename.resolve()}")


if __name__ == "__main__":
    # Check for ffmpeg installation
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("🚨 FFMPEG is not installed or not in your PATH. Please install it to continue.")
        sys.exit(1)
        
    # Check for PyYAML installation
    try:
        import yaml
    except ImportError:
        print("🚨 PyYAML is not installed. Please install it to continue.")
        print("You can install it by running: pip install PyYAML")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Assemble a video from a YAML plan.")
    parser.add_argument("plan_path", help="Path to the video_plan.yaml file.")
    args = parser.parse_args()

    if not Path(args.plan_path).is_file():
        print(f"🚨 Error: Plan file not found at {args.plan_path}")
        sys.exit(1)

    assemble_video(args.plan_path)
