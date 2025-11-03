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
export PATH=$PATH:~/go/bin
just test-chirp
# If  Unauthenticated desc greps, ->
just auth
just gemini-demo-no-auth
/mcp
/aicinema:check_install_modena
```

* Check `GEMINI.md`


# Story of Alessandro

Type `just gemini-demo-no-auth`

## Prompt 1: Create story in 2 languages

```markdown

Crea una storia breve per mio figlio Alessandro, un ragazzo di 7 anni nato a Zurigo di papa' italiano 🇮🇹 e mamma inglese 🇬🇧.
Ama draghi, pokemon, le Tesla ma sopratutto le Ferrari, e infine le pietre preziose (perlopiu' oro e rubini).

Crea una storia spaventosa (ma non troppo) ambientata a Pescara.
Voglio che ci siano dentro questi elementi:
- tanti arrosticini!
- 📚 Gabriele D'Annunzio (e una citazione di una sua poesia almeno 2 versi)
- 🤖 Marvin l'androide paranoico (che sara' la mascotte di Alessandro e fara' da contrappeso tragicomico all'allegria e
spensieratezza del bambino)
- lo zio Fabio, il suo amico di Dublino che fa il programmatore di Ruby.
- lo zio Luca, il suo amico che ama Linux, OSS e Richard Stallman

Lui parla Italiano e Inglese (e Tedesco).

Usa la cartella 📁 `out/pescara/demo01-alessandro-story-derek/`.

Comincia creando una storia in Markdown in inglese (`story-en.md`), poi traducila anche in Italiano.

Infine estrai da queste storie il testo, rimuovendo ogni formattazione (tipo "## titolo H2" o **grassetto**).
Salva questi nuovi file come `story-en.txt`, `story-it.txt`, ...

```

Test: `Verify the 2 italian and 2 english files are in the aforementioned directory. Then proceed.`

## Prompt 2: Create Audio files (Chirp MCP)


```markdown

Ora crea un file sonoro per ciascuna lingua e dagli un nome appropriato (eg, story-en.wav, story-it.wav, ... )

Tutti i file devono essere nella stessa 📂 cartella, ovviamente!

Siccome la mia audience e' italiana, suona automaticamente il file italiano sul mio computer (probabilmente un Mac).

```

## prompt 3 / 4: Create Images (Imagen MCP) and update MD files

```markdown

Ora crea un'immagine che abbia a che fare con la storia, una attinente ad ogni paragrafo: `image1.png`,  `image2.png`, ..

Siccome la API di Gemini non produce bambini, e nel caso tu trovi errori, assicurati che non ci siano "7 year old" o "boy" nella descrizione, e che l'output sia in formato cartone animato in stile Pixar.
```

After the images are created, let's add them to the markdown files.

```

Now patch the  markdown storyfiles by including the images in the proper place.
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
