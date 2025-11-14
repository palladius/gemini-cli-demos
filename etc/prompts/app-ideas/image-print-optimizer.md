## Context

I print a few images for my son: Magic the Gathering cards, pictuers and such. Mostly JPG and PNG. I currently copy paste them into a Google doc and I print them.
Sometimes, for the most precious, I then plastify with my wife plastificatior and cut them all. Paper and plastic papers are expensive, so we want to optimize the colored/printed surface vs white surface (wasted).

## App Design

I would like to create a CLI script, like this:

```bash
./image-print-optimizer -f pics-folder/ --[no-]draw-borders --size [small|medium|large|all] --page-format A4 --paper-border [1cm|100px|1%]
```

The script should then generate a PDF (eg, `out/pics-folder.SIZE.pdf`) which optimizes the size for print space (minimize white space for pics). Let's say you have 4x 4/3 images, it would probably put them in 2x2 in proper size. If you have 3 identical, probably 1x3 where 3 is along the long side, and so on.

It would use some sort of Operations Research algorithm to optimize those images, or maybe try a few random scenarios.
Every solution would have a mathematical.
It would also print the total wasted space with and without border (A4 size, and  A4 minus borders), something like "89% overall, 95% including borders specs).

The script should have the ability to:
1. Support JPG, PNG, ..
2. Ability to draw borders between pics, to help cutting with scissors picture by picture.
3. Support some heuristics of SMALL (eg fit 9 4/3 pics into a single page), MEDIUM (fit ~4 4/3 pics per page) and LARGE (1 pic per page).

Ideally I'd like to see the calculation in stdout (or better in some `out/pics-folder.calculation.txt`, or .log, or .md depending of what you code!).

## Version 1

This is the overall vision. Version 1 should probably:
1. Ignore paper borders for now!
2. ignore page format
3. print size=all (try 3 different pdfs)
4. Initially you can also support JUST 4/3 images, if this makes the algotihm easier. If you support ANY size, all the better.
5. Ignore or minimize the calculation output

## Implementation

1. Start creating a PLAN.md and have user validate it. Iterate until user is happy with design.
2. Whenever implementing a feature, start with a failing test, then implement the test until it works.
3. I will provide a test folder: `test-images/` so you can iterate quickly over it. Ask user if they're satisfied with it. You might want to inspect the PDF yourself, as Gemini is multimodal, and see how much white space there is for a quick AI turnaround.
4. If you choose python, use `uv` and a toml to embed the libraries and forget the `.venv` nightmare. If you choose ruby, even better (use `rbenv` then)!
5. Have a `CHANGELOG.md` and a `VERSION` somewhere (wither in a VERSION file or inside some json or toml)
6. Use `justfile` for `just test` and `just optimize-sample-folder` and other sample invocations.
