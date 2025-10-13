## initial axctions

## On the day - 1h before (once)

Ensure you open this folder:

`code ~/git/gemini-cli-demos/demos/mcp-video-creation`

* Set up `just auth`
* Set up Path
  * `export PATH=$PATH:~/go/bin`
* Check `just test-chirp`
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


## Story of Alessandro

Type `just gemini-demo-no-auth`

```markdown

Crea una storia breve per mio figlio Alessandro, un ragazzo di 7 anni nato a Zurigo di papa' italiano 🇮🇹 e mamma inglese 🇬🇧.
Ama draghi, pokemon, le Tesla ma sopratutto le Ferrari, e infine le pietre preziose (perlopiu' oro e rubini).

Crea una storia spaventosa (ma non troppo) ambientata a Modena.
Voglio che ci siano dentro questi elementi:
- 🖤 l'aceto Balsamico
- 🏎️ una Ferrari elettrica
- 🤖 Marvin l'androide paranoico (che sara' la mascotte di Alessandro e fara' da contrappeso tragicomico all'allegria e
spensieratezza del bambino)

Lui parla Italiano e Inglese (e Tedesco).

Usa la cartella 📁 `out/demo01/ale-modena04oct-prod/`.

Comincia creando una storia in Markdown in inglese (`story-en.md`), poi traducila anche in Italiano.

Infine estrai da queste storie il testo, rimuovendo ogni formattazione (tipo "## titolo H2" o **grassetto**).
Salva questi nuovi file come `story-en.txt`, `story-it.txt`, ...
```

## Audio - prompt2

```
Ora crea un file sonoro per ciascuna lingua e dagli un nome appropriato (eg, story-en.wav, story-it.wav, ... )

Tutti i file devono essere nella stessa 📂 cartella, ovviamente!

Siccome la mia audience e' italiana, suona automaticamente il file italiano sul mio Mac.
```

## Crea Immagini - prompt 3

```markdown
Ora crea un'immagine che abbia a che fare con la storia, una attinente ad ogni paragrafo: `image1.png`,  `image2.png`, ..

Siccome la API di Gemini non produce bambini, e nel caso tu trovi errori, assicurati che non ci siano "7 year old" o "boy" nella descrizione, e che l'output sia in formato cartone animato in stile Pixar.
```

After the images are created, let's add them to the MD:

```
Now patch the  markdown storyfiles by including the images in the proper place. Make sure the image link is correct and not broken so we have a nice story flow.
```

## Video

```
Finally create a video which consitutes a Trailer of this story
Always remember to omit the kid's age/nature to avoid censorship.
```

























## [REMOVEME] one off for the slides


╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│  > Finally create a README.md which contains a mermaid graph containing all the files I've created. I need this for the presentation of a  │
│    demo. Something showing the structure and lofic: prompt -> 3 stories in 3 languages, then 3 sounds, then images based on the EN story,  │
│    and then video based on EN story. With arrows. I'll use an image of it, so it should be visually pelasing.                              │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
