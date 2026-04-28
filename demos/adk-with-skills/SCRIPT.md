
## Creation of initial code

```markdown
<!-- This is the first for initial code creation -->

I want to create an Character Consistency agent which can do character Consistency of Riccardo doing crazy stuff, 
called "Banana Ric".

Use `adk-dev-guide` and `adk-python` skills to develop this ADK agent.

The Agent needs to be able to use skills. See https://adk.dev/skills/ for docs.
It will be able to call this Nano Banana skill with Character Consistency for its author: `~/git/gemini-cli-palladius-public-goodies/skills/nano-banana-ricc/`. If unavailable, clone it it via `git clone https://github.com/palladius/gemini-cli-palladius-public-goodies/` and make it part of the agent itself.

Ensure its working by issuing some sort of 

1. **LLM API KEY test**: `echo How are you? | adk cli run ...`.
2. **Skill test**:  `echo Run the Nanobanana python script with --help and show me the options for image size | adk cli run ...`.

Iterate until it passes both tests. This will make image creation test much easier:

3. **Image creation test**: `echo Create an image of Riccardo eating an Avocado with an ADK label on it | adk cli run ...`.

```



## Check image creation

TODO(ricc):

## Deploy to GEAP

I'd love to see it on GEAP :)