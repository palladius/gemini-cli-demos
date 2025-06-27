I am a Developer Advocate for Google Cloud.

**IMPORTNT** As such, I want to be able to collect all assets that I created - with a focus on JUST "Google Cloud" or "Google" topics: no personal travels, personal blogs, and stuff. Just work.

## Where these Assets are visualized

1. These assets should be currently visible in this github repo


## Some of my online presence:

Feel free to update this list if you find more:

A list of online presence is in this file: `RICCARDO.md`

## What I want you to do

Your work only exists in `output/`


### output/data.yaml

Go to the internet and search for any asset created by Riccardo Carlesso and add it to `output/data.yaml`

Usually an asset is related to an event, for example Riccardo could talk about a "Children stories with Gemini" at a Ruby Day in Verona. We want to capture both, but most importantly the asset itself: title, description, link to a video, and so on.

Every asset should have the following fields:

Assets stanza: ("assets: ..." followed by an array):

* Title (STR): title of the presentation/talk/demo
* AssetType (STR): type: Presentation, Talk, Keynote, demo, ..
* Abstract (STR): abstract of the talk - possibly in the 500 character ballpark (but use whatever you have)
* Publication Date (DATE): when was this info published, video published, website published.
* Event Date (Date): maybe it was published in november, but the event was in october and you can see it from metadata? Great, put it there
* URLs: array of relevant url
* AssetURL: URL for the asset (presentation, pdf, or just a link to the event website mentioning speaker riccardo talking about XXX)
* VideoURL: URL for video (if exists)
* Tags (ARRAY of STRINGS): an array of strings with no spaces (use underscores), for example: "gcp, genai, sre, ruby, ruby_on_rails, travel, italy".

Events stanza: ("events: ..." followed by an array):
* event_title (STR): eg "Ruby Day Verona"
* event_series (STR): eg "Ruby Day"
* event_counter (STR): complements the event title, if the event is yearly, probably the year "2025" if monthly its more "Sep 2025" and so on. It needs to be something that together with the series uniquely identifies the event.
* event_date (DATE): when it happened
* event_place (STR): where it happened. This string should be Google Map searchable, at the very least "City, Country", better if you know more like the final address. Dont assume context, like "Hotel Logonovo" - use full address.
* event_description (STR):

### output/README.md

While the YAML is going to be consumed by a program, this is for essential reading.

**Events**

1. Put a list of events/travels associated to the assets you've found. Take inspiration by https://github.com/palladius/my-sessions-and-bio . These should have an emoji witht he flag of the event country.
2. they should all be linked to the best URL that signify that event in that day. Bonus points if it lists also the speakers for the day.

**Talks**

2. Put also a list of assets (talks, videos, demos..) in bullet points, this should be concise, title only and link to the URLS. Use emoji/emojis for the country/countries where I presented this. These assets should contain: event name and date where they were presented, and the TYPE (demo, talk, CfP ..). Some talks might just be CFPs and so not materialized yet.


## output/assets/images/

If you find a link to a resourcem like the image of a presentation that has been done, this is cheap and precious, so: DOWNLOAD IT! Let's download images rationally, this way:

1. Path should be something like `output/assets/images/[events|talks|workshops|..]/image-name.{png,jpg,..}
2. This path should also be used in the "image: " stanza under both the YAML and the `index.md`. This should allow us to call that image directly from the `index.md` and load that directly (by just removing the initial `output/`).

## Future

<IGNORE>
== IGNORE THIS PART - its for future versions ==

* Propose a PR to https://github.com/palladius/my-sessions-and-bio , or a change in local FS `~/git/my-sessions-and-bio/`.
* make this properly multitennant, allowing multiple people RICCARDO.md, GUILLAUME.md, ... this requires that `output/` becomes `output/NAME_SURNAME/`.

== STOP IGNORING HERE ==
</IGNORE>

## Bugs

* If the WebFetch times out, consider using something as simple as a `curl URL`. Even better,
  consider curling websites under `.cache` with a smart naming which starts with the timestamp of the curl so we can clean or refresh old data. Maybe by creating a `.cache/YYYYMMDD/` :)

## Feedback Loop

* If a date or a location are unknown, please make an effort to fetch the right URL and find that! this is your PRIMARY job, you have time to go around the internet and find stuff. So please find. If AFTER looking well you still can't find a date, and only AFTER searching in the proper event/talk websites, then you can ask user to tip you date or location.
