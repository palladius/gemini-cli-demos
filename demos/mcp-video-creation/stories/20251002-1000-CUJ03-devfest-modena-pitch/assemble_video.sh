#!/bin/bash

# This script assembles the final video for the DevFest Modena 2025 pitch.

BASE_DIR="/Users/ricc/git/gemini-cli-demos/demos/mcp-video-creation/stories/20251002-1000-CUJ03-devfest-modena-pitch"

# Scene 1
ffmpeg -i "$BASE_DIR/veo-veo-3.0-fast-generate-preview-20251002-163027-0.mp4" -i "$BASE_DIR/scene1_music.wav" -c:v copy -c:a aac -shortest "$BASE_DIR/scene1_final.mp4"

# Scene 2
ffmpeg -i "$BASE_DIR/veo-veo-3.0-fast-generate-preview-20251002-163029-1.mp4" -i "$BASE_DIR/scene2_music.wav" -c:v copy -c:a aac -shortest "$BASE_DIR/scene2_final.mp4"

# Scene 3
ffmpeg -i "$BASE_DIR/veo-veo-3.0-fast-generate-preview-20251002-163028-0.mp4" -i "$BASE_DIR/scene3_music.wav" -c:v copy -c:a aac -shortest "$BASE_DIR/scene3_final.mp4"

# Scene 4
ffmpeg -i "$BASE_DIR/veo-veo-3.0-fast-generate-preview-20251002-163030-1.mp4" -i "$BASE_DIR/scene4_music.wav" -c:v copy -c:a aac -shortest "$BASE_DIR/scene4_final.mp4"

# Scene 5
ffmpeg -i "$BASE_DIR/veo-veo-3.0-fast-generate-preview-20251002-163028-0.mp4" -i "$BASE_DIR/scene5_music.wav" -c:v copy -c:a aac -shortest "$BASE_DIR/scene5_final.mp4"

# Concatenate all scenes
ffmpeg -i "$BASE_DIR/scene1_final.mp4" -i "$BASE_DIR/scene2_final.mp4" -i "$BASE_DIR/scene3_final.mp4" -i "$BASE_DIR/scene4_final.mp4" -i "$BASE_DIR/scene5_final.mp4" \
-filter_complex "[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a][4:v][4:a]concat=n=5:v=1:a=1[v][a]" \
-map "[v]" -map "[a]" "$BASE_DIR/devfest_modena_pitch.mp4"