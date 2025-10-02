#!/bin/bash

# This script assembles the final video for the DevFest Modena 2025 pitch.

BASE_DIR="/Users/ricc/git/gemini-cli-demos/demos/mcp-video-creation/stories/20251002-1000-CUJ03-devfest-modena-pitch"

# Scene 1
ffmpeg -i "$BASE_DIR/scene01/veo-veo-3.0-fast-generate-preview-20251002-164353-0.mp4" -i "$BASE_DIR/scene01/scene1_music.wav" -c:v copy -c:a aac -shortest "$BASE_DIR/scene01/scene1_final_new.mp4" -y

# Scene 2
ffmpeg -i "$BASE_DIR/scene02/veo-veo-3.0-fast-generate-preview-20251002-164823-0.mp4" -i "$BASE_DIR/scene02/scene2_music.wav" -c:v copy -c:a aac -shortest "$BASE_DIR/scene02/scene2_final_new.mp4" -y

# Scene 3
ffmpeg -i "$BASE_DIR/scene03/veo-veo-3.0-fast-generate-preview-20251002-164933-0.mp4" -i "$BASE_DIR/scene03/scene3_music.wav" -c:v copy -c:a aac -shortest "$BASE_DIR/scene03/scene3_final_new.mp4" -y

# Scene 4
ffmpeg -i "$BASE_DIR/scene04/veo-veo-3.0-fast-generate-preview-20251002-165054-0.mp4" -i "$BASE_DIR/scene04/scene4_music.wav" -c:v copy -c:a aac -shortest "$BASE_DIR/scene04/scene4_final_new.mp4" -y

# Scene 5
ffmpeg -i "$BASE_DIR/scene05/veo-veo-3.0-fast-generate-preview-20251002-165147-0.mp4" -i "$BASE_DIR/scene05/scene5_music.wav" -c:v copy -c:a aac -shortest "$BASE_DIR/scene05/scene5_final_new.mp4" -y

# Concatenate all scenes
ffmpeg -i "$BASE_DIR/scene01/scene1_final_new.mp4" -i "$BASE_DIR/scene02/scene2_final_new.mp4" -i "$BASE_DIR/scene03/scene3_final_new.mp4" -i "$BASE_DIR/scene04/scene4_final_new.mp4" -i "$BASE_DIR/scene05/scene5_final_new.mp4" -filter_complex "[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a][4:v][4:a]concat=n=5:v=1:a=1[v][a]" -map "[v]" -map "[a]" "$BASE_DIR/devfest_modena_pitch_final.mp4" -y
