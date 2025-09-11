# 1. Storyboard

We want to pitch an event.

## event details

* Language: English
* Location: Rimini, Italy
* Event Title: "Rubycon 2026"
* Date: Fri 8 May 2026
* Details: a community-driven event for Ruby developers. Strong technical agenda and great party in the evening!
* Pitch: Join us for an event
* CTA: "Join our newsletter: https://rubycon.it/" (but make it short in video!)
* Additional URLs for inspiration:
  * http://rubycon.it/
* Imagery:
  * Hotel room (Sala Quarzo, hotel Ambasciatory): https://rubycon.it/assets/images/sala-quarzo.jpg
  * Rubycon logo: [rubycon-logo.png](https://rubycon.it/assets/images/logo.png)

* Elements which should be present:
  * Ruby Logo.
    * Note: using the wording "red diamonds" (diamond pentagonal shape) might result in more realistic images than real rubies (round).
  * We're working on a pun here: "A Ruby Conf" on the "Rubicon" river, near Rimini.
  * Let's make sure Caesar is crossing the Rubicon river with his soldiers, and some Ruby  is in it. This might have a majestic music yet a hilarious twist.
  * [Matz](https://en.wikipedia.org/wiki/Yukihiro_Matsumoto) (Yukihiro Matsumoto, Japanese computer scientist, born 1965) is the creator of the programming language Ruby. Would be nice
    to add some trolling like a Japanese 60-old smiling scientist with glasses wearing a japanese clothing or a Toga. Note that using the exact name might result in Image model failing
    to visualize. Try anonmizing and maybe using a cartoon instead.
  * There's going to be a Toga party (yes, Blutarski Animalhouse style) in the evening. Nothing crazy, like a diverse crowd at a discotheque by the Rimini sea - in the evening.
    * The toga of ALL the attendants will be held together by a ruby brooch.
  * We also want to build a "serious" take of people attending with interest speakers talking about ruby in a splendid grand room.
    * You can use this image for the presentation, and fill it with people: https://rubycon.it/assets/images/sala-quarzo.jpg

## Execution

* Create a folder with name like `YYYYMMDD-HHMM-CUJ03-title-of-story/`.
  * Create a README.md file in it.
* The final video should be around 30-40 seconds at most.

## Storyboard

* Now lets create a storyboard for this story and then N videos from it.
* output the storyboard into `YYYYMMDD-HHMM-title-of-story/storyboard.md`
  * Each scene (6-8sec scene) should be in a H2 ("## Scene XX: ...") so easy to isolate
  * It should contain both the the context AND the prompt.
  * Videos might be ugly, we might need to be able to redo them at a later time so "recast scene4" is something we should be able to do easily, hence this convention.
* If in interactive mode, validate output with user; if not, proceed.
* Be prescriptive of which scene should have music, and which should have audio, eg characters speaking.
  * If a conversation among 2+ people, use **Veo3** to generate audio.
  * If music, use MCP Lyria tools.
  * If a lot of audio needs to be deterministically added to the scene, maybe better to use Chirp model and tool.
* The storyboard should contain instructions for further AUDIO computation, so explain which model should be used depending on the use.
* Do not exaggerate with text on the single videos, no more than 2-3 words in it, or it gets imprecise.
  * If more needs adding, we can do it in post-production with online tools. Just make sure this is in some TODO() for later.

## Iterating the scenes

For each scene, do this (eg for scene 1):

1. Take scene 1 from Markdown
2. Create "2" videos for this scene and call it `scene1_takeX.mp4` for each take.
   1. Use the Veo 3 fast model for both takes.
3. Add info about this to the `README.md` in a table. the table should contain:
   1. scene_time_start (seconds), eg 00:00 (note, its incremental! 0-7 then 8-15 then 16-23 depending if its 8sec or less)
   2. scene_time_end (seconds), eg 00:07 (note, its incremental!)
   3. Short description (max 7 words)
   4. Link to the file (take1)
   5. Prompt used (in italic)
   6. A screenshot of the video, using `ffmpeg` or better `bin/extract_frames.py`.

## Add the audio


## Final merge

Once done,

1. Merge the videos in a single video.
   1. For each scene, you can ask user to evaluate the best, or choose a random one.
   2. The readme should link the CHOSEN take (eg scene1_take2, scene2_take1, ..) for ease of reproduction.
2. Update the README with link to final video and summarize what it's about.
3. Add an `assmeble_video.sh` which contains the deterministic FFMPG command to generate the final video starting from the original ones, so user can tweak the result.
