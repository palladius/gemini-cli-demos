# Demo: ADK from Scratch (Visual & Audio)

## Goal

Demonstrate how Gemini can help explore a new SDK (ADK Python), visualize its architecture, and make it accessible through translation and audio.

## Setup

Ensure the output directory exists:

```bash
mkdir -p out
```

## Step 1: Exploration

1. **Download the ADK**:

```markdown
<!-- Download the ADK locally (Riccardo way). Should -->

Download ADK python repo and ADK Docs, both repos should be under the rag/ folder.
```

1. **Understand the Repo** (AGY way):
   Ask Gemini to explain what this repo does and save it to a file.
   > "Look at the `rag/adk-python` folder. What is this project about? Summarize its core functionality. Save the response to `out/01_summary.md`.
   > Does this repo contain Tests? Evals? Does it explain MCP? And are the docs in here too, or just in the rag/adk-docs/ folder?"

## Step 2: Visualizing the Docs

1. **Create a Markdown/Mermaid Diagram**:

   > "Read the documentation in `adk-python/docs`. Create a Mermaid.js diagram showing the high-level architecture of the ADK (Agents, Tools, Model). Save the mermaid code wrapped as markdown onto `out/02_architecture.md`. Add emojis to the diagram to make it more engaging."

   - _Visual Alternative_:
     > Use `generate_diagram` from Nanobanana MCP to create a visual diagram and save to `out/02_architecture.png`. Use the "Create Diagram" instructions from the nanobanana README: https://github.com/gemini-cli-extensions/nanobanana . Since we are in Geneva, use the `gemini-3-pro-image-preview` model and add some Swiss Romande touch to the final image (could be imagery or text, but needs to be visible!).

<!--
## Step 3: Animation (Bonus)

1. **Animate the Diagram**:
   > "Read `out/02_architecture.md`. Create a text description/script of how you would animate this diagram to explain the request flow. Save this script to `out/03_animation_script.md`."

Note this is not feasible without the Hussain MediaGen MCP , which seems beyond the purpose of this.
-->

## Step 4: Accessibility (Geneve Plan)

1. **Translate to French**:

   > "Read `out/01_summary.md`. Translate the summary to French, and SHORTEN it to a couple of sentences. Save it to `out/04_summary_fr.md`."

2. **Generate Audio**:

   > "Read `out/04_summary_fr.md`. Use the `run_command` tool to generate an audio file using the macOS `say` command. The command should be something like: `say -v Thomas -f out/04_summary_fr.md -o out/05_audio.aiff`."
   > On Linux, use espeak -v fr

   - _Note_: `say` is a native macOS tool (offline, no external APIs).
   - _Note_: For Linux you might weant to use `espeak` instead. `espeak -v fr` should be able to speak French, but its very basic and metallic.

## Step 5: Vibe Coding a Simple Agent

To show how easy it is to get started, we'll create a simple "Hello World" agent with a single tool.

> "Create a new directory `out/vibecoded_agent`. Inside it, create a simple ADK agent named `hello_agent`. The agent needs a tool called `fancy_hello` that takes no arguments and returns the string 'Hello from your friendly ADK Agent! 🚀'. The agent's instruction should be to use this tool to greet the user. Also, create the necessary `__init__.py` file.
> Before handing over to me, ensure that it doesnt have any syntax errors, by issuing "just test-vibecoded-demo-agent" until it works!"

After the files are created, you can run the agent with:

```bash
just test-vibecoded-demo-agent
adk run out/vibecoded_agent/
```

You can then type a greeting like "Hello" and the agent should respond with the fancy greeting from its tool.
