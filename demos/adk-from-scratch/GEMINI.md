## About

We want to do the following demo to demonstrate Gemini CLI:

1. Download
2. Generate docs
3. Run

TODO(Ricc or AGY): perfect this readme

## Rules

1. Everything you download from the itnernet whihc is fungible, put it under `tmp/`. If it's augmenting your knowledge, put it under `rag/`. We'll git-ignore tmp/ but not rag/ to allow you to keep your knowledge.
2. All output from scripts should go to `out/` which we're nicely git-ignoring :)
3. Never call `gemini` via shell!
4. Never overwrite `.env` (just ensure it exists or pinpoint the error to the user)
5. Never code with "gemini-1.5-flash" model: any model below 2.0 is obsolete now. I suggest to use "gemini-2.5-flash" or more.

## Resources

- ADK in python: https://github.com/google/adk-python
- ADK documentation GH repo: https://github.com/google/adk-docs
  - They can be read online in: https://google.github.io/adk-docs/
- Official nanobanana extension: https://github.com/gemini-cli-extensions/nanobanana
  - Use the latest model: check `.env` contains it.
  - Install: `gemini extensions install https://github.com/gemini-cli-extensions/nanobanana`
  - To create diagrams, check "Create Diagrams:" in [readme](https://github.com/gemini-cli-extensions/nanobanana?tab=readme-ov-file#-usage).
