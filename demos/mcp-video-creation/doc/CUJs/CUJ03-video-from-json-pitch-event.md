# 1. Storyboard

We want to pitch an event.

## event details

* Language: Italian
* Location: Modena, Italy
* Event Title: "Dev Fest Modena"
* Date: Sat 4 Oct 2025.
* Details: a community free event, with plenty of technical talks around the Google ecosystem. One of the biggest
  events in Italy
* Pitch: Something Join us for an event
* CTA: subscribe to the event for free at https://devfest.modena.it/

## Execution

* Create a folder with name like `YYYYMMDD-HHMM-CUJ03-title-of-story/`.
* The final video should be around 30-40 seconds at most.

## Storyboard

* Now lets create a storyboard for this story and then N videos from it.
* output the storyboard into `YYYYMMDD-HHMM-title-of-story/storyboard.md`
  * Each scene (6-8sec scene) should be in a H2 ("## Scene XX: ...") so easy to isolate
  * It should contain both the the context AND the prompt.
  * Videos might be ugly, we might need to be able to redo them at a later time so "recast scene4" is something we should be able to do easily, hence this convention.
* If in interactive mode, validate output with user; if not, proceed.

## Iterating the scenes

For each scene, do this (eg for scene 1):

1. Take scene 1 from Markdown
2. Create "2" videos for this scene and call it `scene1_takeX.mp4` for each take.
   1. Use the Veo 3 fast model for both takes.
3. Add info about this to the `README.md` in a table. the table should contain:
   1. scene_time_start (seconds), eg 00:00
   2. scene_time_end (seconds), eg 00:07
   3. Short description (max 7 words)
   4. Link to the file
   5. Prompt used (in italic)

Once done,

1. Merge the video in a single video.
2. Update the README with link to final video and summarize what it's about.
