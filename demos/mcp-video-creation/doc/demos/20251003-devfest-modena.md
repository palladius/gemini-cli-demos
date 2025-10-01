## initial axctions

## On the day - 1h before (once)

Ensure you open this folder:

`code ~/git/gemini-cli-demos/demos/mcp-video-creation`

* Set up `gcloud auth`
* Check `just test-chirp`
* Set up Path
  * `export PATH=$PATH:~/go/bin`
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
Crea una storia per mio figlio Alessandro, un ragazzo di 7 anni nato a Zurigo di papa' Italiano e mamma inglese.
Ama draghi, pokemon, le tesla ma sopratutto le ferrari, e infine le pietre preziose.
Crea una storia spaventosa ma non troppo ambientata a Modena. Voglio che ci siano dentro questi elementi:
- Pavarotti
- l'aceto Balsamico
- una Ferrari elettrica

Lui parla  Italiano, Inglese e Tedesco.

Use folder `out/ale-modena/`.

Crea una storia in Markdown in inglese (`story-en.md`), poi traducila anche in Italiano e Tedesco.

Infine estrai da queste storie il testo, rimuovendo ogni formattazione (tipo "## titolo H2" o **grassetto**).
Salva questi nuovi file come `story-en.txt`, `story-it.txt`, ...
```

## Audio

Ora crea un file sonoro per ciascuna di queste storie e dagli un nome appropriato (eg, story-en.wav, story-it.wav, ... )

Tutti i file devono essere nella stessa 📂 cartella, ovviamente!

Siccome la mia audience e' italiana, suona automaticamente quello italiano sul mio computer

## Immagine

Ora crea un'immagine che abbia a che fare con la storia, una per l'inizio e una per il finale. Di ciascuna immagine voglio 4 versioni ("num_images":4).

* start-1.png, ..
* finale-1.png, ..

Siccome la API di Gemini non produce bambini, assicurati che non ci siano "7 year old" o "boy" nella descrizione, e che l'output sia in formato cartone animato tipo Pixar.

## Video

Infine costruisci un video che faccia da trailer su questa storia.
Ricorda sempre di omettere l'eta' del bimbo.
