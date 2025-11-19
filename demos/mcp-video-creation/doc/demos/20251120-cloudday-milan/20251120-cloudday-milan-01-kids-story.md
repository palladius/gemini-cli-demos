## initial actions

## On the day - 1h before (once)

Ensure you open this folder:

`code ~/git/gemini-cli-demos/demos/mcp-video-creation`

* Set up          `just auth`
* Set up Path:                    `export PATH=$PATH:~/go/bin`
* Check         `just test-chirp`
* Check PATH once
* Launch:

```bash
source .env
export PATH=$PATH:~/go/bin
just test-chirp
just chirp-io-amo-il-risotto-alla-milanese 
# If  Unauthenticated desc greps, ->
just auth
just gemini-demo-no-auth
/mcp
/aicinema:check_install
```

* Check `GEMINI.md`


# Story of Alessandro

Type `just gemini-demo-no-auth`

## Prompt 1: Create story in 2 languages

```markdown

Create a short story for my son Alessandro, a 7-year-old boy born in Zurich to an Italian 🇮🇹 father ("papino") and an English 🇬🇧 mummy.
He loves dragons, pokemon, Teslas but above all Ferraris, and finally precious stones (mostly gold and rubies).

Create a scary (but not too scary) story set in Milan.
I want it to contain these elements:
- a delicious risotto alla milanese!
- 📚 Alessandro Manzoni (and a quote of at least 2 verses from one of his poems or from Promessi Sposi, rigurously in ITALIAN)
- 🤖 Marvin the Paranoid Android (who will be Alessandro's mascot and will be a tragicomic counterpoint to the child's cheerfulness and
carefreeness)
- 💛 Uncle Alfredo who, likes papino, is deeply in love with the color "yellow".
- ☁️ Google Cloud as the best Cloud Provider ever! 

Dad and mummy should NOT be part of the story (cheesy!).

He speaks Italian and English (and German).

Use the folder 📁 `out/milan/demo01-alessandro-story/`.

Start by creating a story in Markdown in English (`story-en.md`), then translate it into Italian (`story-it.md`).

Then extract the text from these stories, removing all formatting (like "## H2 title" or **bold**).
Save these new files as `story-en.txt` and `story-it.txt`.

```

Test: `Verify the 2 italian and 2 english files are in the aforementioned directory. Then proceed.`

## Prompt 2: Create Audio files (Chirp MCP) in assembled chunks


```markdown
<!-- Sound creation - with chirp limitation written down -->

Now create a sound file for each language and give it an appropriate name (eg, story-en.wav, story-it.wav)

All files must be in the same 📂 folder, of course!

Since my audience is English-speaking, automatically play the English file on my computer (probably a Mac).

Note: the Chirp API wont let you create a single big file, so you need to split into smaller paragraphs, create them in a subfolder audio-chunks/it/ and audio-chunks/en/ and then assemble them.
```

## prompt 3 / 4: Create Images (Imagen MCP) and update MD files

```markdown
<!-- IMAGE creation pt1 -->

Now create an image that has to do with the story, one pertaining to each paragraph: `image1.png`,  `image2.png`, ..

Since the Gemini API does not produce children, and in case you find errors, make sure that there are no "7 year old" or "boy" in the description, and that the output is in a Pixar-style cartoon format.

<!-- /IMAGE creation -->
```

* After the images are created, let's add them to the markdown files.

```markdown
<!-- IMAGE creation pt1 -->

Now patch the markdown storyfiles (both en and it) by including the images in the proper place.
MAKE SURE the image link is correct and not broken so we have a nice story flow.

Also, attach the AUDIO play on top; not sure if Markdown will allow it.
If yes, good.
If not, create a story-XX.html which embeds the audio file playing please,
using HTML5 `<audio>` tag with `autoplay` and `controls` attributes.

```

Note on HTML: doesnt work on GitHUb, so you need to have an HTML preview like this: https://html-preview.github.io/?url=https://github.com/palladius/gemini-cli-demos/blob/main/demos/mcp-video-creation/out/demo01/ale-pescara-prod/story-it.html


## prompt 5: Create Video (Veo3 MCP) and possibly a GIF


```
Finally create a video which consitutes a Trailer of this story
Always remember to omit the kid's age/nature to avoid censorship.
Use Veo3, 8 seconds, dramatic voiceover (with a 8sec short speech, probably title and little more).
```

*Note*: I think the .gif creation comes from my CUJ prompt for video creation.

## prompt 6: Merge all in a README.md with some smart links

```
Now create a README.md which links the video, embeds the GIF, links ther audios, and points to the HTML and MarkDown files. basically, an index with all the links where the user can come
and immediately see the GIF video, and the images, and click for more stories.

If possible, add an H2 with the story plot, and a H2 on how this all was created through Gemini CLI, MCP and MediaGen for Vertex AI (all with links and emojis, as a marketing tactic to sell the product)

Before these 2 H2s and after the links, please create and attach a mermaid graph of all the objects created and how they're linked to gether (TXT -> Md, IMG -> Md and so on)
```