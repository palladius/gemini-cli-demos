# AI Reasoning

This document outlines the decisions made by the AI agent while processing the data for the Gemini CLI monitoring project.

## GitHub Issues

- I used the `gh` CLI to fetch the issues from the `google-gemini/gemini-cli` repository.
- I created a Python script to process the downloaded JSON data and create the `issues.csv` and `issues.md` files.
- The script performs a simple sentiment analysis based on keywords in the issue title and body.

## Stack Overflow Questions

- I attempted to fetch the questions directly from the Stack Overflow website, but it was blocked.
- I used the Stack Exchange API to get the questions tagged with `gemini-cli`.
- I created a Python script to process the JSON response and create the `stackoverflow.csv` file.

## Reddit Posts

- I was unable to fetch the Reddit posts automatically.
- I manually created the `reddit.csv` file with some sample data.
