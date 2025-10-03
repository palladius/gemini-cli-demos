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

```markdown

Crea una storia per mio figlio Alessandro, un ragazzo di 7 anni nato a Zurigo di papa' italiano 🇮🇹 e mamma inglese 🇬🇧.
Ama draghi, pokemon, le Tesla ma sopratutto le Ferrari, e infine le pietre preziose (perlopiu' oro e rubini).

Crea una storia spaventosa (ma non troppo) ambientata a Modena.
Voglio che ci siano dentro questi elementi:
- Pavarotti
- l'aceto Balsamico
- una Ferrari elettrica
- Marvin l'androide paranoico (che sara' la mascotte di Alessandro e fara' da contrappeso tragicomico all'allegria e
spensieratezza del bambino)

Lui parla Italiano, Inglese e Tedesco.

Usa la cartells 📁 `out/ale-modena02/`.

Comincia creando una storia in Markdown in inglese (`story-en.md`),
poi traducila anche in Italiano e Tedesco.

Infine estrai da queste storie il testo, rimuovendo ogni formattazione (tipo "## titolo H2" o **grassetto**).
Salva questi nuovi file come `story-en.txt`, `story-it.txt`, ...
```

## Audio

```
Ora crea un file sonoro per ciascuna di queste storie e dagli un nome appropriato (eg, story-en.wav, story-it.wav, ... )

Tutti i file devono essere nella stessa 📂 cartella, ovviamente!

Siccome la mia audience e' italiana, suona automaticamente il file italiano sul mio Mac.
```

## Immagine

```
Ora crea un'immagine che abbia a che fare con la storia, una per l'inizio e una per il finale. Di ciascuna immagine voglio 4 versioni ("num_images":4).

* start-1.png, ..
* finale-1.png, ..

Siccome la API di Gemini non produce bambini, assicurati che non ci siano "7 year old" o "boy" nella descrizione, e che l'output sia in formato cartone animato tipo Pixar.
```

## Video

```
Infine costruisci un video che faccia da trailer su questa storia.
Ricorda sempre di omettere l'eta' del bimbo.
```




## one off for the slides

╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│  > Finally create a README.md which contains a mermaid graph containing all the files I've created. I need this for the presentation of a  │
│    demo. Something showing the structure and lofic: prompt -> 3 stories in 3 languages, then 3 sounds, then images based on the EN story,  │
│    and then video based on EN story. With arrows. I'll use an image of it, so it should be visually pelasing.                              │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
