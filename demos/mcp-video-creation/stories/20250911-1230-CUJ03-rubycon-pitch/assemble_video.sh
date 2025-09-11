#!/bin/bash

ffmpeg -i scene1_final.mp4 -i scene2_final.mp4 -i scene3_take2.mp4 -i scene4_final.mp4 -i scene5_final_simple_cta.mp4 \
-filter_complex "[0:v:0][0:a:0][1:v:0][1:a:0][2:v:0][3:v:0][3:a:0][4:v:0][4:a:0]concat=n=5:v=1:a=1[outv][outa]" \
-map "[outv]" -map "[outa]" rubycon_pitch_final.mp4