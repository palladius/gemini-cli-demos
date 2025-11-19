## initial actions

You've finished the demo01, now demo 02 in testing mode.


###

```bash
just gemini-demo-no-auth         # or just gemini-demo-with-auth the first time
```


Maybe test `list_chirp_voices in Italian via MCP` to test authentication.


```markdown
<!-- during the day - short time -->
/aicinema:video_storyboard Take inspiration from the pitch event described in @doc/demos/20251120-cloudday-milan/event-pitch.md . Create a compelling 3-scene storyboard for a teaser video in Italian, inspired by the themes and content of the Cloud Day event (URL: https://www.cloudday.it/). The storyboard should be saved as `STORYBOARD.md` in the designated output folder.

Make sure to dump all your thinking in MD in a designated folder under `out/milan/demo02/` which contains today's YYYYMMDD-HHMM, in case we get interrupted 😉. 
For simplicity, use a SINGLE take per video, and rename videos to `sceneXX.mp4` after creation.

```

#### Some tips / addons

During the day, if needed, add: 

`This is for a quick demo, so use fastest models.`

Or, if you get interrupted: 

```markdown
Note we *DID* get interrupted, so the folder already exists ;) Check under `out/milan/demo02/` for existing files and take it from there.
```

## More structured prompt (alternative)

Add this more structured structure:

```
  Maybe you could group the scenes in folders? scene02/README.md would have the Music, video and image prompt and all takes. Maybe a symlink should allow us to seamlessly choose the "good one" among multiple takes.
  You can choose the first, and ask user to maybe choose another, and finally the construction of the final video could be seamless:

* For scene 1, create folder `scene01/`
    *  `README.md` containing Image, text, Video prompt and post-generation text to add, eg: `"Welcome to <LOCATION>>" on the bottom center in big character`.
    * `video_take01.mp4` For the first video take
    * `video_take02.mp4`
    * `video_take03.mp4`
    * `music01.wav`
    * `music02.wav` ..  in case we need more..
    * `assembled_video_final.mp4` which contains the final assembly of video + music + [optionally] a Post generation text.
* For scene 2 create folder `scene02/`
  * .. and so on
* For the assempled stuff (production video) you can use something like "production/" which will assembles scene1/2/3/4 into a single piece.
* In the base folder you have a bash script which assembles all the `scene*/assembled_video_final.mp4` into the `production/` folder; this can be called again in case we want to change or retake a video.
```

## Thursday prep prompts.




* Re do the CTA video using deterministic TXT injection and not MCP/Veo:

```
both teasers v2 and v3 have the wrong scene4 TEXT - you need to do better there :) The @out/milan/demo02/20251119-1000-CloudDayMilan-Pitch/scene4_image.png  has an AMAZING          
  background. The only broken thing is the URL, which is probably the most important. Can you remove it and add it deterministically (not sure if ffmped allows image editing, i know  
  you can definitely do it in a video - and maybe that's the thing. Maybe we mcake it appear from 2 to 6 sec.                                                                          
                                                                                                                                                                                       
```