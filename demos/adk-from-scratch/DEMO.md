# Demo: ADK from Scratch (Visual & Audio)

## Goal

Demonstrate how Gemini can help explore a new SDK (ADK Python), visualize its architecture, and make it accessible through translation and audio.

## Setup

Ensure the output directory exists:

```bash
## Clean
just clean # rm rag/* and out/*
mkdir -p out
just run
```

## Step 1: Exploration

1. **Download the ADK**:

```markdown
<!-- Download the ADK locally (Riccardo way). Should -->
Download ADK python repo and ADK Docs, both repos should be under the rag/ folder.
```

1. **Understand the Repo** (AGY way):    Ask Gemini to explain what this repo does and save it to a file. 
   > "Look at the `rag/adk-python` folder. What is this project about? Summarize its core functionality. Save the response to `out/01_summary.md`.
   > Does this repo contain Tests? Does it explain MCP? And are the docs in here too, or just in the rag/adk-docs/ folder?"
   > Explain to me how I would do a Travel agent which dispatches wotk to other subagents: flights, hotels, and restaurants and finally a budget agent to keep track of the budget expenditure based on the price of the flights, hotels, and restaurants. save this under `out/01_travel_agent.md`. I want both small snippets of code AND a high level overview of the architecture possibly with mermaid.

## Step 2: Visualizing the Docs

1. **Create a Markdown/Mermaid Diagram**:

   > "Read the documentation in `rag/adk-docs/`. Create a Mermaid.js diagram showing the high-level architecture of the ADK (Agents, Tools, Model). Save the mermaid code wrapped as markdown onto `out/02_architecture.md`. Add emojis to the diagram to make it more engaging."

2. **Create a PNG image with NanoBanana**:

   > Use `generate_diagram` from Nanobanana MCP to create a visual diagram and save to `out/02_architecture.png`. Use the "Create Diagram" instructions from the nanobanana README: https://github.com/gemini-cli-extensions/nanobanana . Since we are in Geneva, use the `gemini-3-pro-image-preview` model and add some Swiss Romande touch to the final image (could be imagery or text, but needs to be visible!).
   > Do the same for the Travel Agent file `out/01_travel_agent.md`.
   > Concentrate on its architecture and the link between main agent and sub agents =>  `out/02_travel_agent_architecture.png`

## Step 3: Accessibility (Geneve Plan)

1. **Translate to French**:

   > "Read `out/01_summary.md`. Translate the summary to French, and SHORTEN it to a couple of sentences. Save it to `out/03_summary_fr.md`."

2. **Generate Audio**:

   > "Read `out/03_summary_fr.md`. Use the `run_command` tool to generate an audio file using the macOS `say` command. The command should be something like: `say -v Thomas -f out/03_summary_fr.md`."
   > Make sure that the text is prepended by a short salutation to the folks in Geneva in a cold winter day.

   - _Note_: `say` is a native macOS tool (offline, no external APIs).
   - _Note_: For Linux you might weant to use `espeak` instead. `espeak -v fr` should be able to speak French, but its very basic and metallic.
   - _Note_: Make sure to speak it out loud for max effect in the demo

## Step 4: Vibe Coding a Simple Agent

To show how easy it is to get started, we'll create a simple "Hello World" agent with a single tool.

> "Create a new directory `out/vibecoded_agent`. Inside it, create a simple ADK agent named `hello_agent`. The agent should have a `get_time_now()` tool that returns the current time in JSON format, together with "status": "success". The agent's instruction should be to use this tool to greet the user. Also, create the necessary `__init__.py` file.
> Also create a second tool like `where_am_i()` which uses an online API to return the current location of the user. Maybe a simple `curl -s ipinfo.io/json` suffices.
> Before handing over to me, ensure that it doesnt have any syntax errors, by issuing "just test-vibecoded-demo-agent" until it works!"

After the files are created, you can run the agent with:

```bash
just test-vibecoded-demo-agent
adk run out/vibecoded_agent/
```

You can then type a greeting like "Hello" and the agent should respond with the fancy greeting from its tool.
