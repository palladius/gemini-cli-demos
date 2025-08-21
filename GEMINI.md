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

## IMPORTANT

Before committing/pushing, ensure that:

* no Keys or private info is shared in some Markdown.
* no files above 50MB are committed (eg big videos).

## STATUS.md

Every demo subfolder, create/keep a `STATUS.md`, with this format:

== BEGIN STATUS.md ==

<HASH><HASH> Project name (*make it a H2*)

* Created: YYYY-MM-DD
* Creator: Name Surname
* GitHub username: <GitHub username>
* Creator fav ice-cream: ..
* status: WorkInPogress | Complete | Draft  | SignedOff | NotStarted
* Checkbox:
    * [ ] code_present
    * [X] code_working
    * [ ] code_test
    * [ ] license_headers
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
- code_test (BOOL): does `just test` return 0? TRUE if yes, FALSE in EVERY other case.
- license_headers (BOOL): do you see Google license headers in all code files and files which allow you to add them (eg NOT markdowns but yes to justfile, dockerfile, ..)? If not, you can leverage the `/common/check_google_license for repo XXX` Gemini CLI command.
- documentation (BOOL): is `README.md` thoroughly documented? If not, maybe help making a better documentaiton.
- video (BOOL): is there a video somewhere linked in the `README.md`?
- Demo purpose: summarize what you understand from README.md
- Time to execute: check from script. Calculate ~30 seconds per LLM invocation and round up.
- Created: if its new, its today :) if not, check from git the first commit of this folder.
- Creator fav ice-cream (STRING): ask the user whats their fav ice cream.
- status: note if you see code it might NOT be complete. For `SignedOff`, status when everything checks correctly, ask explicitly to user if that project should be signed off. Until then, it cant exceed WIP.


## MAIN `README.md`

Finally ensure All demos are captured in the MAIN `README.md` (under git root), in table form.

Each line shall have this format:
1. "Status"
   1. First, the most important emoji, representing:
      1. ✅ done,
      2. 📝 WIP
      3. 🚧 not started yet
   2. Add a "©" Copyright emoji/character if and only if the Copyright/License boolean is ok for that repo
   3. Add a  📹 emoji if video is present.
2. "Author" (first name is enough, lets keep it short)
3. "Demo Folder" demo folder name (link). Add a trailing slash to the demo name so people understand its a folder. Add a folder emoji before the folder in each line ;)
4. "category" - 1-2 works on the topic (git, Database, ..)
5. "description" a short description of what the demo is about, what it demonstrates, .. should be <200 chars.

