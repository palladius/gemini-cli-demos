#!/bin/bash

# This script assembles scene 1 with the third take.

BASE_DIR="/Users/ricc/git/gemini-cli-demos/demos/mcp-video-creation/stories/20251002-1000-CUJ03-devfest-modena-pitch"

ffmpeg -i "$BASE_DIR/veo-veo-3.0-fast-generate-preview-20251002-164353-0.mp4" -i "$BASE_DIR/scene1_music.wav" -c:v copy -c:a aac -shortest "$BASE_DIR/scene1_final_take3.mp4"
