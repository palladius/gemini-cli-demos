#!/bin/bash

ffmpeg -i stories/20250911-1230-CUJ03-rubycon-pitch/scene1_final.mp4 -i stories/20250911-1230-CUJ03-rubycon-pitch/scene2_take2.mp4 -i stories/20250911-1230-CUJ03-rubycon-pitch/scene3_take2.mp4 -i stories/20250911-1230-CUJ03-rubycon-pitch/scene4_final.mp4 -i stories/20250911-1230-CUJ03-rubycon-pitch/scene5_new.mp4 \
-filter_complex "[0:v:0][0:a:0][1:v:0][1:a:0][2:v:0][3:v:0][3:a:0][4:v:0]concat=n=5:v=1:a=1[outv][outa]" \
-map "[outv]" -map "[outa]" stories/20250911-1230-CUJ03-rubycon-pitch/rubycon_pitch_new.mp4
