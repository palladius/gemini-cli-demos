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
<!-- Download the ADK locally -->
Download https://github.com/google/adk-python under the rag/ folder
```


1. **Understand the Repo**:
   Ask Gemini to explain what this repo does and save it to a file.
   > "Look at the `adk-python` folder. What is this project about? Summarize its core functionality. Save the response to `out/01_summary.md`."

## Step 2: Visualizing the Docs

1. **Create a Diagram**:
   > "Read the documentation in `adk-python/docs`. Create a Mermaid.js diagram showing the high-level architecture of the ADK (Agents, Tools, Model). Save the mermaid code to `out/02_architecture.mmd`."

   * *Alternative*: Use `generate_image` to create a visual diagram and save to `out/02_architecture.png`.

## Step 3: Animation (Bonus)

1. **Animate the Diagram**:
   > "Read `out/02_architecture.mmd`. Create a text description/script of how you would animate this diagram to explain the request flow. Save this script to `out/03_animation_script.md`."

## Step 4: Accessibility (Geneve Plan)

1. **Translate to French**:
   > "Read `out/01_summary.md`. Translate the summary to French. Save it to `out/04_summary_fr.md`."

2. **Generate Audio**:
   > "Read `out/04_summary_fr.md`. Use the `run_command` tool to generate an audio file using the macOS `say` command. The command should be: `say -v Thomas -f out/04_summary_fr.md -o out/05_audio.aiff`."

   * *Note*: `say` is a native macOS tool (offline, no external APIs).
