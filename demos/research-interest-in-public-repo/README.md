# 🔎 Research Interest in Public Repositories

This project aims to monitor and analyze public discussions related to a public project you just launched on GitHub (eg, Gemini CLI) across various platforms. In this use case, the goal is to gather insights into community sentiment, identify common issues, and facilitate quick responses from the Cloud DevRel team.

* **🎯 Scope** This tool focuses exclusively on content related to the **Gemini CLI** product. Any information outside this scope is ignored.

## 📊 Monitored Platforms

We monitor the following platforms for Gemini CLI discussions:

*   **GitHub Issues**: [https://github.com/google-gemini/gemini-cli/issues](https://github.com/google-gemini/gemini-cli/issues)
*   **Stack Overflow**: [https://stackoverflow.com/questions/tagged/gemini-cli](https://stackoverflow.com/questions/tagged/gemini-cli)
*   **Reddit**: [https://www.reddit.com/](https://www.reddit.com/)

## 🗄️ Data Storage

Collected data is stored locally to ensure persistence and enable incremental updates. The data is organized as follows:

*   `.cache/`: Volatile data, not checked into Git.
*   `output/`: Final processed output, intended for user consumption.
*   `data/`: Larger datasets, structured in YAML format with subfolders for each platform (e.g., `data/github/`, `data/reddit/`).

## 🚀 How to Use

This project is designed to be invoked multiple times, picking up from where it left off. The scripts in the `bin/` directory handle data collection and processing.

