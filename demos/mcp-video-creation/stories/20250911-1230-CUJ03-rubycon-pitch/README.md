# Rubycon Pitch Video

This folder contains the assets for the Rubycon pitch video.

## Storyboard

The storyboard for the video can be found in [storyboard.md](storyboard.md).

## Video Scenes

| scene_time_start | scene_time_end | Short description | Link to the file (take1) | Prompt used |
|---|---|---|---|---|
| 00:00 | 00:08 | Roman legion crossing the Rubicon | [scene1_take1.mp4](scene1_take1.mp4) | *A photorealistic video of Roman legionaries, led by Julius Caesar, crossing the Rubicon river. The legion's standards are adorned with large, sparkling red diamonds in a pentagonal shape. The sky is dramatic. Cinematic, 8k.* |
| | | | [scene1_take2.mp4](scene1_take2.mp4) | |
| 00:08 | 00:16 | Japanese computer scientist in a toga | [scene2_take1.mp4](scene2_take1.mp4) | *A cartoon-style animation of a smiling, 60-year-old Japanese computer scientist with glasses, wearing a Roman toga. He is holding a large, glowing red diamond. The background is a serene Japanese garden.* |
| | | | [scene2_take2.mp4](scene2_take2.mp4) | |
| 00:16 | 00:24 | Conference room with developers | [scene3_take1.mp4](scene3_take1.mp4) | *A professional, corporate-style video of a conference room filled with a diverse audience of developers. The room is the 'sala quarzo' from the Rubycon website. A speaker is on stage, with a presentation slide showing the Ruby logo. The audience is engaged and taking notes.* |
| | | | [scene3_take2.mp4](scene3_take2.mp4) | |
| 00:24 | 00:32 | Toga party by the sea | [scene4_take1.mp4](scene4_take1.mp4) | *A vibrant, energetic video of a toga party at a discotheque by the sea in Rimini at night. A diverse crowd of people in togas are dancing and having fun. Everyone's toga is held together by a glowing red ruby brooch. The atmosphere is festive and exciting.* |
| | | | [scene4_take2.mp4](scene4_take2.mp4) | |
| 00:32 | 00:40 | Rubycon logo and call to action | [scene5_take1_simple_cta.mp4](scene5_take1_simple_cta.mp4) | *An animated graphic of the Rubycon logo, with the text 'rubycon.it' and a subscribe button. The video should evolve from the provided map image.* |
| | | | [scene5_take2_simple_cta.mp4](scene5_take2_simple_cta.mp4) | |

## Final Video

The final video can be found here: [rubycon_pitch_final.mp4](rubycon_pitch_final.mp4)

This video is a pitch for the Rubycon conference in Rimini, Italy. It features a mix of majestic and humorous scenes, including a Roman legion crossing the Rubicon, the creator of Ruby in a toga, a professional conference setting, and a vibrant toga party. The video concludes with a call to action to join the conference newsletter.

**Note:** Scene 3 of the video is silent. You can use the provided `assemble_video.sh` script to add your own audio to this scene and regenerate the final video.

## Production Notes

### Why generate videos one-by-one?

You asked why I called the video generation tool twice with `"num_videos": 1` instead of once with `"num_videos": 2`.

Calling the tool for each take individually provides more granular control. It allows me to rename the output file immediately after it's created, which helps keep the project organized and makes it easier to track which video corresponds to which take. While calling it once with `num_videos: 2` is more efficient, the one-by-one approach is a safer workflow for managing multiple scenes and takes. However, per your request, I will use the more efficient method going forward.

## Riccardo notes

If I have to do it again, some notes:

1. Wrong dates.
2. Wrong language: it -> en
3. Toga take 2 is better than take 1.
4. I really don't like scene 5, but we can do it with Vids.
