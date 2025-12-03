# Project Summary: Agent Development Kit (ADK) for Python

## 📋 Overview
The **Agent Development Kit (ADK)** is an open-source, code-first Python framework designed for building, evaluating, and deploying sophisticated AI agents. It emphasizes software development principles, offering a modular and flexible approach to agent creation. While it is optimized for Google's **Gemini** models, it remains model and deployment agnostic.

## 🔑 Core Functionality
*   **Agent Creation**: Define agents using Python code, allowing for versioning, testing, and flexibility.
*   **Multi-Agent Systems**: Support for hierarchical and modular agent structures, enabling the composition of specialized agents (e.g., coordinators, task executors).
*   **Tool Integration**: Capabilities to integrate pre-built tools, custom functions, OpenAPI specifications, and MCP (Model Context Protocol) tools.
*   **Configuration**: Options to build agents via configuration files (no-code/low-code approach).
*   **Deployment**: Ready for deployment on Google Cloud Run or Vertex AI Agent Engine.
*   **Evaluation**: Built-in tools for evaluating agent performance (`adk eval`).
*   **Vibe Coding**: Includes context files (`llms.txt`, `llms-full.txt`) to assist LLMs in understanding the codebase for "vibe coding" workflows.

## 📚 Documentation Location
The documentation is distributed as follows:

*   **Source Code**: The core library resides in `rag/adk-python`.
*   **Documentation Source**: The comprehensive user documentation is located in **`rag/adk-docs/docs`**.
    *   This folder contains the source files for the documentation site (likely built with MkDocs).
    *   It covers topics like Getting Started, Agent Configuration, Tools, and Tutorials.

> **Note**: You can find the official hosted documentation at [google.github.io/adk-docs](https://google.github.io/adk-docs/).
