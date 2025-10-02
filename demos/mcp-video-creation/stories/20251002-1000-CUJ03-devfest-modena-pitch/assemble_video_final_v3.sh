#!/bin/bash

# This script assembles the final video for the DevFest Modena 2025 pitch.

BASE_DIR="/Users/ricc/git/gemini-cli-demos/demos/mcp-video-creation/stories/20251002-1000-CUJ03-devfest-modena-pitch"

# Concatenate all scenes
ffmpeg -i "$BASE_DIR/scene01/scene1_final_new.mp4" -i "$BASE_DIR/scene02/scene2_final_new.mp4" -i "$BASE_DIR/scene03/scene3_final_new_with_audio.mp4" -i "$BASE_DIR/scene04/scene4_final_new.mp4" -i "$BASE_DIR/scene05/scene5_final_new_v2.mp4" \
-filter_complex "[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a][4:v][4:a]concat=n=5:v=1:a=1[v][a]" \
-map "[v]" -map "[a]" "$BASE_DIR/devfest_modena_pitch_final_v3.mp4" -y
