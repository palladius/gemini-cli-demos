## initial actions

You've finished the demo01, now demo 02 in testing mode.

###

```bash
just gemini-demo-no-auth         # or just gemini-demo-with-auth the first time
```

Maybe test `list_chirp_voices in  British English via MCP` to test authentication.


```markdown

/aicinema:video_storyboard for the story highlighted
in @doc/CUJs/CUJ03c-video-from-pitch-event-mythos2510.md
Make sure to dump all your thinking in MD in a designated folder
under `out/demo-mythos/`
which contains today's YYYYMMDD-HHMM, in case we get interrupted 😉.
For simplicity, use a SINGLE take per video,
and rename videos to sceneXX.mp4 after creation.

Note: This is for a quick demo, so use fastest models.
```

If needed: `This is for a quick demo, so use fastest models.`

Or:

```
Note we DID get interrupted, so the folder already exists ;) Check under stories/ and take it from there
```

Add this more structured structure:

```
  Maybe you could group the scenes in folders? scene02/README.md would have the Music, video and image prompt and all takes. Maybe a symlink should allow us to seamlessly choose the "good one" among multiple takes.
  You can choose the first, and ask user to maybe choose another, and finally the construction of the final video could be seamless:

* For scene 1, create folder `scene01/`
    *  `README.md` containing Image, text, Video prompt and post-generation text to add, eg: `"Welcome to Mythos" on the bottom center in big character`.
    * `video_take01.mp4` For the first video take
    * `video_take02.mp4`
    * `video_take03.mp4`
    * `music01.wav`
    * `music02.wav` ..  in case we need more..
    * `assembled_video_final.mp4` which contains the final assembly of video + music + [optionally] a Post generation text.
* For scene 2 create folder `scene02/`
* .. and so on
* In the base folder you have a bash script which assembles all the `scene*/assembled_video_final.mp4`; this can be called again in case we want to change or retake a video.
```
