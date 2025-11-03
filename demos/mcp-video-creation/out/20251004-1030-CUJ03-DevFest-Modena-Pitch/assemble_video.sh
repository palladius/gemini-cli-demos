#!/bin/bash

# Define input files
VIDEO_SCENE1="scene01_take01.mp4"
VIDEO_SCENE2="scene02_take01.mp4"
VIDEO_SCENE3="scene03_take01.mp4"
VIDEO_SCENE4="scene04_take01.mp4"
VIDEO_SCENE5="scene05_take01.mp4"

MUSIC_SCENE1="scene1_music.wav"
MUSIC_SCENE2="scene2_music.wav"
MUSIC_SCENE3="scene3_music.wav"
MUSIC_SCENE4="scene4_music.wav"
MUSIC_SCENE5="scene5_music.wav"

VOCAL_SCENE1="scene1_vocal_snippet-en-US-Chirp3-HD-Zephyr-20251004-071814.wav"
VOCAL_SCENE5="scene5_call_to_action-en-US-Chirp3-HD-Zephyr-20251004-072718.wav"

OUTPUT_DIR="/Users/ricc/git/gemini-cli-demos/demos/mcp-video-creation/20251004-1030-CUJ03-DevFest-Modena-Pitch"
FINAL_VIDEO="${OUTPUT_DIR}/final_devfest_modena_pitch.mp4"

# 1. Concatenate video scenes
ffmpeg -i "${OUTPUT_DIR}/${VIDEO_SCENE1}" -i "${OUTPUT_DIR}/${VIDEO_SCENE2}" -i "${OUTPUT_DIR}/${VIDEO_SCENE3}" -i "${OUTPUT_DIR}/${VIDEO_SCENE4}" -i "${OUTPUT_DIR}/${VIDEO_SCENE5}" \
-filter_complex "[0:v:0][0:a:0][1:v:0][1:a:0][2:v:0][2:a:0][3:v:0][3:a:0][4:v:0][4:a:0]concat=n=5:v=1:a=1[outv][outa]" \
-map "[outv]" -map "[outa]" "${OUTPUT_DIR}/concatenated_video_only.mp4"

# 2. Concatenate music tracks
ffmpeg -i "${OUTPUT_DIR}/${MUSIC_SCENE1}" -i "${OUTPUT_DIR}/${MUSIC_SCENE2}" -i "${OUTPUT_DIR}/${MUSIC_SCENE3}" -i "${OUTPUT_DIR}/${MUSIC_SCENE4}" -i "${OUTPUT_DIR}/${MUSIC_SCENE5}" \
-filter_complex "[0:a:0][1:a:0][2:a:0][3:a:0][4:a:0]concat=n=5:v=0:a=1[outa]" \
-map "[outa]" "${OUTPUT_DIR}/concatenated_music.wav"

# 3. Combine concatenated video and music
ffmpeg -i "${OUTPUT_DIR}/concatenated_video_only.mp4" -i "${OUTPUT_DIR}/concatenated_music.wav" \
-c:v copy -map 0:v:0 -map 1:a:0 "${OUTPUT_DIR}/video_with_music.mp4"

# 4. Layer vocal snippets
ffmpeg -i "${OUTPUT_DIR}/video_with_music.mp4" \
       -i "${OUTPUT_DIR}/${VOCAL_SCENE1}" \
       -i "${OUTPUT_DIR}/${VOCAL_SCENE5}" \
       -filter_complex "[1:a]adelay=0|0[a1]; [2:a]adelay=28000|28000[a2]; [0:a][a1][a2]amix=inputs=3:duration=longest[outa]" \
       -map 0:v -map "[outa]" -c:v copy -c:a aac -b:a 192k "${FINAL_VIDEO}"

echo "Final video assembled at: ${FINAL_VIDEO}"