
## Scripts

* If you happen to do some non trivial use of `ffmpeg` or avtool or other tools, please write reusable code under `bin/`
  by making it reusable while minimizing the number of arguments.

* Whenever you do a video, use `ffmpeg_video_to_gif` to also make a gif of same name! They're more portable.
* I've noticed sometimes you tend to


## Video collaction

I'd be particularly interested in constructing some middleware to set up the video collation in some way.
This could be a CSV/AVRO/JSON Containing all the relevant info so we can deterministically calculate things.
On top of my head:
* The final video contains an array of scenes and becomes the juxtaposition of them
  * every scene is a Veo3 output, constrained to 8sec max.
  * Every scene can have N takes.
  * .. Maybe a music
  * .. Maybe an audio in those ~8sec.
* We might have a story audio track maybe spans over multiple scenes. Maybe the audio is 2min and pieces of it need to be adjusted to fit those scenes.
    * Maybe the story output in Chirp should be transformed into text with the time of text, like in `.srt` format

```
1
00:00:01,500 --> 00:00:04,200
This is the first caption block.

2
00:00:05,000 --> 00:00:08,800
And this is the second one.
```

### Desired output

this is complex and error prone! I'd like to have some sort of DB or "plan" where we say:

* 00:00-00:07
  * Video: Use `scene1_take2.mp4`
  * Music: Use `music1.wav`
  * Audio: Just use the native audio from `scene1_take2.mp4`

* 00:08-00:15
  * Video: Use `scene2_take3.mp4`
  * Music: No music
  * Audio: Use the narrator voice from 00:00-00:07 from `chirp-2minutes.wav`

If we had some sort of text-based database (I'm currently thinking of a JSON / some elaborated CSV), then the LLM
can try to create a video, and the user can just tweak a couple of things in the "recipe" and then some bash/python script
can assemble everything together based on the "desired state". yes, like a `kubectl apply` :)
Yes probably a `yaml` sounds best!

## Additional features

* Support for video with `starting_image: room.png` and/or `ending_image: room.png`.
* Support for overlaying TEXT on top of existing image. we can use the Nano Banana model for this: first generate the image without text, then trying a few times to add text (note: LLM added text is instrinsically error prone, particularly in a video).
* Supporting for

## Misc

* Do not use `gsutil`, its broken for me. Use `gcloud storage ..` instead.
* Use `"num_videos":2` to generate TWO videos with `veo_t2v`
