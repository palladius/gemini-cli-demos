#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video Assembler Script

This script reads a YAML file that defines a video structure (scenes, audio, etc.)
and uses ffmpeg to assemble the final video and a companion GIF.

Usage:
    python3 bin/assemble_video.py /path/to/your/video_plan.yaml
"""

import argparse
import os
import shutil
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

def create_gif_from_video(video_path, temp_dir):
    """Creates a high-quality GIF from a video file."""
    print(f"\n🖼️ Creating GIF for {video_path.name}...")
    gif_path = video_path.with_suffix('.gif')
    palette_path = Path(temp_dir) / "palette.png"

    # GIF settings
    fps = 15
    scale_width = 540

    # 1. Generate color palette for high-quality GIF
    palette_cmd = [
        'ffmpeg', '-i', str(video_path),
        '-vf', f"fps={fps},scale={scale_width}:-1:flags=lanczos,palettegen",
        '-y', str(palette_path)
    ]
    run_ffmpeg_command(palette_cmd)

    # 2. Create GIF using the generated palette
    gif_cmd = [
        'ffmpeg', '-i', str(video_path),
        '-i', str(palette_path),
        '-filter_complex', f"fps={fps},scale={scale_width}:-1:flags=lanczos[x];[x][1:v]paletteuse",
        '-y', str(gif_path)
    ]
    run_ffmpeg_command(gif_cmd)
    print(f"🎉 GIF creation complete! Output file: {gif_path.resolve()}")


def assemble_video(plan_path):
    """Main function to assemble the video based on the YAML plan."""
    
    plan_path = Path(plan_path).resolve()
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

            music_track = scene.get('music')
            narration_track = scene.get('narration')
            final_audio_for_scene = None
            
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

            output_scene_video = Path(temp_dir) / f"scene_{scene_num}_processed.mp4"
            
            if final_audio_for_scene:
                cmd = [
                    'ffmpeg',
                    '-i', str(scene_video),
                    '-i', str(final_audio_for_scene),
                    '-c:v', 'copy',
                    '-c:a', 'aac',
                    '-map', '0:v:0',
                    '-map', '1:a:0',
                    '-shortest',
                    '-y', str(output_scene_video)
                ]
                run_ffmpeg_command(cmd)
            else:
                # If no custom audio, we still process the video to standardize its streams
                # for concatenation. This re-encodes existing audio to AAC or adds a
                # silent AAC track if no audio is present.
                print("ℹ️ No custom audio for this scene. Standardizing video for concatenation.")
                cmd = [
                    'ffmpeg',
                    '-i', str(scene_video),
                    '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=48000',
                    '-c:v', 'copy',
                    '-c:a', 'aac',
                    '-map', '0:v:0',
                    '-map', '1:a:0',
                    '-shortest',
                    '-y', str(output_scene_video)
                ]
                run_ffmpeg_command(cmd)


            processed_scene_files.append(output_scene_video)

        # --- Final Concatenation (Robust Method) ---
        print("\n🎞️ Concatenating all processed scenes...")
        
        # Prepare inputs for the filter_complex command
        inputs = []
        for video_file in processed_scene_files:
            inputs.extend(['-i', str(video_file)])
            
        # Create the filter_complex string (e.g., "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]")
        filter_str = ""
        for i in range(len(processed_scene_files)):
            filter_str += f"[{i}:v][{i}:a]"
        filter_str += f"concat=n={len(processed_scene_files)}:v=1:a=1[v][a]"

        output_filename = Path(plan['output_filename'])
        cmd = [
            'ffmpeg',
            *inputs,
            '-filter_complex', filter_str,
            '-map', '[v]',
            '-map', '[a]',
            '-y', str(output_filename)
        ]
        run_ffmpeg_command(cmd)
        
        print(f"\n🎉 Video assembly complete! Output file: {output_filename.resolve()}")

        # --- Automatic GIF Creation ---
        create_gif_from_video(output_filename, temp_dir)


if __name__ == "__main__":
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("🚨 FFMPEG is not installed or not in your PATH. Please install it to continue.")
        sys.exit(1)
        
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