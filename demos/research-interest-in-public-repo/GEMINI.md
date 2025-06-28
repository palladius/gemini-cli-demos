We recently launched Gemini CLI and we want to monitor ALL the internet noise about it.
We want to see good press, bad press, do some sentiment analysis.
As Cloud Devrel, we also want to be able to respond quickly to questions on the internet.

* github repo: https://github.com/google-gemini/gemini-cli
* Stackoverflow tagged convos: https://stackoverflow.com/questions/tagged/gemini-cli
* Reddit

## Scope

Ignore anything that does NOT relate to the Gemini CLI product!
Do not download locally anything which is out of scope, or if you do feel free to remove that.

## things to monitor

* GH Issues (currently 551): https://github.com/google-gemini/gemini-cli/issues , particularly the ones that still need triage.
* Stackoverflow tagged questions: https://stackoverflow.com/questions/tagged/gemini-cli
* Reddit: https://www.reddit.com/

## How to interact with File System

Make sure all data that you download are under:

* `.cache/`: if intrinsically volatile, and not checked in git
* `output/`: if of interest to final user (me). This should contain a subset of the info and be
* `data/`: for BIGGER things. Be structured, a nicely readable YAML format is preferred. You could have subfolders like
  * `data/github/`
    * `issues.yaml`
    * `pull_requests.yaml`
  * `data/reddit/`
  * `data/{SOMETHING_ELSE}/`

## What's required of you

A gemini CLI script (you) will be invoked multiple times, so it's of paramount importance you're able to pick up from where you leave it. Which is why it's important to persist locally the findings.

You need to find a way (and document it in `AI_REASONING.md`) to download files only once or at most once every X days. Feel free to use the filesystem to download/persist data and summarize them. Find a way to persist them in a way that we can do it again tomorrow.

For instance, I want you to:

* dump GitHUb issues (use `gh` if available, or fetch if not). every issue should have some sort of metrics (upvotes, comments, popularity). dig as much as you can since we have 500+ bugs and no human can see them all.
* Dump Gemini CLI questions on Stackoverflow
* Dump questions on Reddit, record discussions title, subreddit, and so on.

Whenever you make a decision for something which hasn't been defined yet, make sure to add it to `AI_REASONING.md`,
which allows for stateful and consequential updates.

## Requested output

The final output I want is all under `output/` and in the following files:

* `output/issues.csv`: a list of issues with: Id of the issue, title, number of upvotes, and an emoji with a generic sentiment analysis of it (Feature Request, Bug report, Suggestion, ..). Use thumbs up/down for positive/negative sentiment, and a computer emoji if its simply pure code. Sorted by ID DESC. Also add a small (160char max) synopsis of what the bug is about.
  * I also want a boolean if the bug needs triage:  "status/need-triage" tag: (https://github.com/google-gemini/gemini-cli/issues?q=is%3Aissue%20state%3Aopen%20label%3Astatus%2Fneed-triage). If so add a 🚧 emoji.
* `output/issues.md`: This would be a human-readable version of the above, maybe only with the last 50 issues (500 are too many) in DATE DESC. The issues should have the title with a permalink to github issue, eg https://github.com/google-gemini/gemini-cli/issues/XXXX. Crop the title to 64B. The Last 50 issues should form a table where the emoji should be first, linked title second, and whatever you want afterwards. This should have BOTH
  * a list of the LATEST 50 in time DESC order.
  * And a list with the 20 with the most upvotes, in upvotes desc order.
  * And a list with the 20 with the most #comments , in #comments DESC order.
  * If you find other relevant metrics, I'm all ears in AI_RESONING for more tables :)
* `output/reddit.csv`: You decide. Needs to contain a permalink to it, so I can click on it. At least: some popularity metric (upvotes), title, and <160B synopsis.
* `output/reddit.md`: Again, a top 50 list of titles, linked to conversation permalink. They should also contain some sort of sentiment analysis provided by LLM.
* `output/README.md`: Something shows a synopsis of ALL the above MD documents.
  * A link to them
  * Number with statistics of them (N issues, M positive/O negative), ...
  * It would make me VERY happy if there was some sort of pie chart of the issues: red negative, green positive and blue everything else. Feel free to decide how to create it.

## Googlers

You have a list of googlers in `data/googlers.yaml`.
If the owner of a bug on github is a googler, add this emoji (🧢) to the title, if its in the comments, add it to the comments column.

## AI vs determinism

Some things you're required to do can be done programmatically. In that case, if you need to do it multiple times, feel
free to dump bash (or small python) scripts under `bin/`. Do this only if you feel you might benefit from it tomorrow.

Somethings require an LLM (your) reasoning. There are two approaches to it.
1. The easiest is that you use the deterministic approach for the first part (eg, download issues into a CSV) an call it eg "blahblah_deterministic.ext" and then you take this input and do the LLM work (summarization, sentiment analysis yourself)
2. If you see value in repeatedly doing this, feel free instead to CODE something accessing gemini. In this case, put the file in `bin/` and have 'llm' somewhere in the script name.

In CSVs, keep data raw.
In Markdown, make them human friendly. For instance, translate to English from other languages (eg there's a title in chinese ATM). If you DO translate, please add the country flag emoji "closest" to the original language. You choose.
