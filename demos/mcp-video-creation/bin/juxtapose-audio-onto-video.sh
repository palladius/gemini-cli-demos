#!/bin/bash
#
# This script replaces the audio of a video file with a new audio file.
#
# Usage:
#   juxtapose-audio-onto-video.sh [audiofile] [videofile] [outputfile]

set -euo pipefail

AUDIOFILE="$1"
VIDEOFILE="$2"
OUTPUTFILE="$3"

ffmpeg -i "${VIDEOFILE}" -i "${AUDIOFILE}" -c:v copy -map 0:v:0 -map 1:a:0 -shortest "${OUTPUTFILE}"
