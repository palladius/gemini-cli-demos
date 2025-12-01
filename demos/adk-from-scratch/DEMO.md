# Demo: ADK from Scratch (Visual & Audio)

## Goal
Demonstrate how Gemini can help explore a new SDK (ADK Python), visualize its architecture, and make it accessible through translation and audio.

## Step 1: Exploration
1.  **Download the ADK**:
    ```bash
    git clone https://github.com/google/adk-python
    ```
2.  **Understand the Repo**:
    Ask Gemini to explain what this repo does.
    > "Look at the `adk-python` folder. What is this project about? Summarize its core functionality."

## Step 2: Visualizing the Docs
1.  **Read the Documentation**:
    > "Read the documentation in `adk-python/docs` (or `README.md`)."
2.  **Create a Diagram**:
    > "Based on the documentation, create a visual diagram of the ADK architecture. You can use Mermaid.js or generate an image."
    *   *Action*: Use `generate_image` to create a high-level architecture diagram.
    *   *Prompt*: "A clean, modern diagram showing the architecture of the Google ADK Python, including Agents, Tools, and the Model."

## Step 3: Animation (Bonus)
1.  **Animate the Diagram**:
    > "How would you animate this diagram to explain the flow of a request? Create a script or description for an animation."

## Step 4: Accessibility (Geneve Plan)
1.  **Translate to French**:
    > "Summarize the workshop/ADK purpose in French."
2.  **Generate Audio**:
    > "Use the Chirp MCP (or `afplay` with a TTS tool) to read this French summary aloud."
    ```bash
    # Example if using a TTS tool
    say -v Thomas "Bonjour, voici le résumé du kit de développement d'agents."
    ```
