
# Demo EXPERT L14

## Startup / Prep

Ensure the nanobanana MCP is used:

`gemini extensions install https://github.com/gemini-cli-extensions/nanobanana`

## [D&D demo] Showcase MCP

show MCP servers

```
/mcp
```

## prompt 1 - without CC

```
Use Nanobanana to create a D&D character who's eating a banana, in tragicomical way. Use your creativity to infuse life into it
```

## prompt 2 - with CC

Now do it similar, but with the Custom Command:

`/generate a watercolor painting of a puffin in a snowy Zurich`


## Show editing

`now edit the image (created under /nanobanana-output/) adding a "Created with NanoBanana" on bottom in the center, papyrus style.`

This will fail:

✦ I could not find the file /usr/-21/local/google/home/ricc/git/gemini-cli-demos/demos/nanobanana/nanobanana-output/a_puffin_in_a_snowy_zurich_water.png to edit. I looked in the current directory,
  images, input, nanobanana-output, Downloads and Desktop folders.


## find file manually maybe

```ruby
Do a `find .` and find the file
Now add a "Created with NanoBanana" on bottom in the center, papyrus style.
```


```bash
ok now take images in src/ and add a small banana on top right for all images.
```

```
Now take Modena image in src/ and add a Banana and a cute Dwarf eating it.
```


