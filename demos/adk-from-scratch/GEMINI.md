## About

We want to do the following demo to demonstrate Gemini CLI:

1. Download 
2. Help
3. 

## Rules

1. Everything you download from the itnernet whihc is fungible, put it under `tmp/`. If it's augmenting your knowledge, put it under `rag/`. We'll git-ignore tmp/ but not rag/ to allow you to keep your knowledge.
2. All output from scripts should go to `out/` which we're nicely git-ignoring :)

## Resources

* ADK in poython: https://github.com/google/adk-python
* ADK docs: https://google.github.io/adk-docs/
* Official nanobanana extension:  https://github.com/gemini-cli-extensions/nanobanana
    * Use the latest model: export NANOBANANA_MODEL=gemini-3-pro-image-preview  (see .env.dist and copy it to .env IF IT DOESNT EXIST)
    * Install: `gemini extensions install https://github.com/gemini-cli-extensions/nanobanana`

