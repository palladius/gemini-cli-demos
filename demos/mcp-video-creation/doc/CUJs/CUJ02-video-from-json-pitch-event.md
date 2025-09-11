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

* Create a folder with name like `YYYYMMDD-HHMM-title-of-story/`.
  * Copy the `etc/samples/veo.json` into the folder as `YYYYMMDD-HHMM-title-of-story/veo-storyboard.json`
  * Note that this template gives you an animation for 8 seconds.
* The final  last around 30-40 seconds at most.

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
2. Create a file `veo-scene1.json` by copying the `etc/samples/veo.json` and setting all the parameters as needed.
3. Paste this JSON as payload into Veo API with the `veo_t2v` Tool.
