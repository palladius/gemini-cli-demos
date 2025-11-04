#!/bin/bash

# Define input files
INPUT_1="scene1_final.mp4"
INPUT_2="scene2_final.mp4"
INPUT_3="scene3_final.mp4"
INPUT_4="scene4_final.mp4"
INPUT_5="scene5_final.mp4"

# Define output file
OUTPUT_VIDEO="devfest_pescara_promo.mp4"

# Create a file list for ffmpeg concatenation
echo "file '$INPUT_1'" > mylist.txt
echo "file '$INPUT_2'" >> mylist.txt
echo "file '$INPUT_3'" >> mylist.txt
echo "file '$INPUT_4'" >> mylist.txt
echo "file '$INPUT_5'" >> mylist.txt

# Concatenate videos using ffmpeg
ffmpeg -f concat -safe 0 -i mylist.txt -c copy "$OUTPUT_VIDEO"

# Clean up the file list
rm mylist.txt

echo "Video assembled as $OUTPUT_VIDEO"
