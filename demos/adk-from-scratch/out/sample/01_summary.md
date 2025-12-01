**Project Summary:**
The Agent Development Kit (ADK) is an open-source, code-first Python framework for building, evaluating, and deploying sophisticated AI agents. It emphasizes modularity and composition, allowing developers to define agent logic, tools, and orchestration directly in Python code. ADK is model-agnostic and deployment-agnostic, optimized for Gemini but compatible with other frameworks. It simplifies the creation of agents for tasks ranging from simple to complex workflows.

**Core Functionality:**
*   **Agents:** Blueprints defining identity, instructions, and tools (e.g., `LlmAgent`, `LoopAgent`, `ParallelAgent`, `SequentialAgent`).
*   **Tools:** Python functions or capabilities agents can call to interact with the world (e.g., search, API calls, OpenAPI specs, MCP tools, Google API tools).
*   **Runner:** The execution engine orchestrates the "Reason-Act" loop, manages LLM calls, executes tools, and handles multi-agent coordination. It provides `run_async`, `run_live` (bi-directional streaming), and `run` modes.
*   **Session:** Manages conversation state and history for continuous dialogue.
*   **Memory:** Provides long-term recall across different sessions.
*   **Artifact Service:** Manages non-textual data like files.
*   **Evaluation Framework:** Allows for comprehensive testing and evaluation of agents using various metrics and test cases.
*   **Deployment:** Supports deployment to Google Vertex Agent Engine, Google Cloud Run, and Google GKE.
*   **Development UI:** A built-in web UI for testing, evaluating, debugging, and showcasing agents.

**Tests & Evals:**
*   The repository contains extensive tests under the `tests/` directory, including `unittests/` (2600+ unit tests across 236+ files) and `integration/`.
*   It also features an `evaluation/` framework (`src/google/adk/evaluation/` with 47 files) to assess end-to-end performance with live LLMs, using test cases and metrics like `tool_trajectory_avg_score` and `response_match_score`. The `adk eval` CLI command is available for running evaluations.

**MCP Explanation:**
The `rag/adk-python` repository frequently mentions "MCP" (Model Context Protocol) in various `README.md` files within the `contributing/samples/` directory and in the `AGENTS.md` and `README.md` files at the root. It's described as a type of tool (`MCP tools`) that agents can use for integration with external services (e.g., PostgreSQL, Notion) or for advanced functionalities like server-side sampling. The `AGENTS.md` explicitly states `mcp_tool/ # Model Context Protocol` under the `tools/` directory. While it doesn't provide a single, comprehensive definition of MCP in one place, its usage and integration are explained through examples and its role in the tool ecosystem.

**Documentation Location:**
The core documentation for ADK is primarily located at `https://google.github.io/adk-docs/`, as indicated in the `README.md` and `AGENTS.md`. However, the `rag/adk-python` repository itself contains significant internal documentation, including `AGENTS.md`, `CONTRIBUTING.md`, and `adk_project_overview_and_architecture.md` under `contributing/`, along with numerous `README.md` files within the `contributing/samples/` directories, which serve as examples and detailed explanations for various features and integrations.
