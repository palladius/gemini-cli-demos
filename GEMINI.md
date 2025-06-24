This is an official Google Demos repository, so it's essential that it's kep high quality.

Demos are organized under `demos` as follows:

```bash
├── demos
│   ├── git-investigation
│   └── sqlite-investigation
│   └── ...
```

to ensure other folders (bin, doc, assets) don't get confused as demos.


## Quality bar

Ensure:
* all markdown has no typos or obvious mistakes.
* all linked URLs in markdown are publicly available (ensure a curl returns 200).

## STATUS.md

Every demo subfolder, create/keep a `STATUS.md`, with this format:

== BEGIN STATUS.md ==

HASH HASH Project name (H2)

* Created: YYYY-MM-DD
* Creator: Name Surname
* Creator fav ice-cream: ..
* status: WorkInPogress | Complete | Draft | UnderReview
* Checkbox:
    * [ ] code_present
    * [ ] code_working
    * [X] documentation
    * [ ] video
* Demo purpose: ...
* Time to execute: **XX** minutes

== END STATUS.md ==

So anyone can check the status. Check with user for missing information and fill in the blanks.

You should be able to fill in the blanks yourself:
- check Name surname from git
- code present (BOOL): see if there's a DEMO_SCRIPT.md and if it feels right
- code_working (BOOL): does it feel complete?
- documentation (BOOL): is `README.md` thoroughly documented? If not, maybe help making a better documentaiton.
- video (BOOL): is there a video somewhere linked in the `README.md`?
- Demo purpose: summarize what you understand from README.md
- Time to execute: check from script. Calculate ~30 seconds per LLM invocation and round up.
- Created: if its new, its today :) if not, check from git the first commit of this folder.
- Creator fav ice-cream (STRING): ask the user whats their fav ice cream.
