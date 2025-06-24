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

```markdown
## Project name

* Creator: Name Surname
* description:
* status: WorkInPogress | Complete | Draft | UnderReview
* Checkbox:
    * [ ] code present
    * [ ] code working
    * [X] documentation
    * [ ] video
* Demo purpose: [try to infer it if you have anough info, or leave a '-' if not enough info.. info will come!]
```

so anyone can check the status. Check with user for missing information and fill in the blanks.
