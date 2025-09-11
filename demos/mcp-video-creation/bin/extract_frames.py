#!/usr/bin/env python
import subprocess
import os
import argparse

def extract_frames(video_path):
    """
    Extracts one frame per second from a video file using ffmpeg.
    The output directory is created based on the video file's name.
    For example, a video named 'my_video.mp4' will have its frames
    saved in a directory named 'my_video_frames/'.

    Args:
        video_path (str): The absolute path to the input video file.
    """
    # Get the directory and the base name of the video file
    video_dir = os.path.dirname(video_path)
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    
    # Create the output directory path
    output_dir = os.path.join(video_dir, f"{base_name}_frames")

    # Ensure the output directory exists.
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: {output_dir}")

    # This is the ffmpeg command, broken into a list of arguments.
    command = [
        "ffmpeg",
        "-i", video_path,
        "-vf", "fps=1",
        f"{output_dir}/frame_%03d.png"
    ]

    print(f"Running command: {' '.join(command)}")

    try:
        # Execute the command
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )
        print("Successfully extracted frames.")
        print("ffmpeg output:\n", result.stdout)
    except FileNotFoundError:
        print("Error: ffmpeg is not installed or not in your PATH.")
        print("Please install ffmpeg to use this script.")
    except subprocess.CalledProcessError as e:
        print(f"Error during ffmpeg execution. Return code: {e.returncode}")
        print("ffmpeg stderr:\n", e.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract one frame per second from a video. The output directory will be created automatically based on the video name (e.g., 'video.mp4' -> 'video_frames/')."
    )
    parser.add_argument("video_path", help="The absolute path to the input video file.")
    
    args = parser.parse_args()
    
    extract_frames(args.video_path)
