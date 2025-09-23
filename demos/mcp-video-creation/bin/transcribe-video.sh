#!/bin/bash

# This script transcribes a video file to text using ffmpeg and whisper.
# If the video has multiple audio streams, it will create a transcription for each stream.

# Prerequisites:
# 1. Homebrew installed.
# 2. ffmpeg and ffprobe installed (`brew install ffmpeg`).
# 3. whisper installed (`pip3 install git+https://github.com/openai/whisper.git`).

# Usage: ./bin/transcribe-video.sh <video_file>

if [ -z "$1" ]; then
  echo "Usage: $0 <video_file>"
  exit 1
fi

VIDEO_FILE=$1

# The --user flag for pip might mean the executable is in ~/.local/bin
# I will add that to the path
export PATH=$PATH:~/.local/bin
# Also the warning suggested /Users/ricc/Library/Python/3.13/bin
export PATH=$PATH:/Users/ricc/Library/Python/3.13/bin

# Get the number of audio streams
NUM_STREAMS=$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$VIDEO_FILE" | wc -l | xargs)

for (( i=0; i<NUM_STREAMS; i++ )); do
  AUDIO_FILE="${VIDEO_FILE%.*}_stream_$i.wav"
  TRANSCRIPTION_FILE="${VIDEO_FILE%.*}_stream_${i}_transcription.txt"

  # Extract audio from video
  ffmpeg -i "$VIDEO_FILE" -map 0:a:$i -vn -acodec pcm_s16le -ar 16000 -ac 1 "$AUDIO_FILE" -y

  # Transcribe audio using whisper
  whisper "$AUDIO_FILE" --output_format txt --output_dir "$(dirname "$VIDEO_FILE")"

  # Rename the output file
  mv "${VIDEO_FILE%.*}_stream_$i.txt" "$TRANSCRIPTION_FILE"

  # Clean up the temporary audio file
  rm "$AUDIO_FILE"

  echo "Transcription for stream $i written to $TRANSCRIPTION_FILE"
done