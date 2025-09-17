#!/bin/bash

# This script transcribes a video file to text using ffmpeg and whisper.

# Prerequisites:
# 1. Homebrew installed.
# 2. ffmpeg installed (`brew install ffmpeg`).
# 3. whisper installed (`pip3 install git+https://github.com/openai/whisper.git`).

# Usage: ./bin/transcribe-video.sh <video_file>

if [ -z "$1" ]; then
  echo "Usage: $0 <video_file>"
  exit 1
fi

VIDEO_FILE=$1
AUDIO_FILE="${VIDEO_FILE%.*}.wav"
TRANSCRIPTION_FILE="${VIDEO_FILE%.*}_transcription.txt"

# Extract audio from video
ffmpeg -i "$VIDEO_FILE" -vn -acodec pcm_s16le -ar 16000 -ac 1 "$AUDIO_FILE" -y

# Transcribe audio using whisper
# The --user flag for pip might mean the executable is in ~/.local/bin
# I will add that to the path
export PATH=$PATH:~/.local/bin
# Also the warning suggested /Users/ricc/Library/Python/3.13/bin
export PATH=$PATH:/Users/ricc/Library/Python/3.13/bin

whisper "$AUDIO_FILE" --output_format txt --output_dir "$(dirname "$TRANSCRIPTION_FILE")"

# Rename the output file
mv "${AUDIO_FILE%.*}.txt" "$TRANSCRIPTION_FILE"

# Clean up the temporary audio file
rm "$AUDIO_FILE"

echo "Transcription written to $TRANSCRIPTION_FILE"
