#!/usr/bin/env python3
import csv
import yaml
import json
import google.generativeai as genai
import os
from dotenv import load_dotenv
from google.api_core.exceptions import GoogleAPIError, NotFound

load_dotenv()

# Configure the Gemini API key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if GEMINI_API_KEY:
    print("Gemini API key found.")
    genai.configure(api_key=GEMINI_API_KEY)
else:
    print("Gemini API key not found. Please set the GEMINI_API_KEY environment variable and try again.")
    exit(1) # Exit if API key is not found

GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")
print(f"Using Gemini model: {GEMINI_MODEL}")

def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(prompt)
        return response.text
    except NotFound as e:
        return f"Error: Gemini model 'gemini-pro' not found or not accessible. Please check your API key, region, and model availability. Details: {e}"
    except GoogleAPIError as e:
        return f"Error from Gemini API: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def generate_llm_insights():
    insights_content = "# LLM-Generated Insights\n\n"

    # Load issues data from JSON
    issues_data = []
    try:
        with open('/Users/ricc/git/gemini-cli-demos/demos/research-interest-in-public-repo/data/github/issues.json', 'r') as f:
            issues_data = json.load(f)
    except FileNotFoundError:
        insights_content += "Error: data/github/issues.json not found. Please run process_issues.py first to fetch GitHub issues.\n"
        with open('/Users/ricc/git/gemini-cli-demos/demos/research-interest-in-public-repo/output/LLM_INSIGHTS.md', 'w') as f:
            f.write(insights_content)
        return

    print(f"Loaded {len(issues_data)} issues. Preparing prompt for LLM...")

    # Construct the comprehensive prompt
    prompt_parts = [
        "You are an expert in analyzing GitHub issues. Your task is to summarize a list of issues and identify potential duplicates or highly similar issues. For each identified duplicate group, explain why they are considered duplicates and suggest a course of action.",
        "\n\nHere is the list of GitHub issues, each with a numeric ID (issue number), Title, and Body:",
        "\n\n---"
    ]

    for issue in issues_data:
        prompt_parts.append(f"ID: {issue['number']}\nTitle: {issue['title']}\nBody: {issue['body']}\n---")

    prompt_parts.append("\n\nYour output should be in Markdown format, structured as follows:")
    prompt_parts.append("\n## Issue Summaries")
    prompt_parts.append("For each issue, provide a concise summary (2-3 sentences).")
    prompt_parts.append("\n## Potential Duplicate Issues")
    prompt_parts.append("List groups of issues that are duplicates or highly similar. For each group, provide:")
    prompt_parts.append("- The IDs and Titles of the issues in the group, with permalinks to their GitHub pages (e.g., [Title](https://github.com/google-gemini/gemini-cli/issues/ID)).")
    prompt_parts.append("- A brief explanation of why they are duplicates/similar.")
    prompt_parts.append("- A 'Course of Action:' bullet point suggesting how to handle them (e.g., 'Merge A into B', 'Close A as duplicate of B', 'Cross-reference A and B').")
    prompt_parts.append("\n## General Insights and Course of Action")
    prompt_parts.append("Provide any other general insights or recurring themes you notice, and suggest overall courses of action.")

    full_prompt = "\n".join(prompt_parts)

    print("Sending prompt to LLM...")
    llm_response = get_gemini_response(full_prompt)

    if "Error generating content" in llm_response:
        insights_content += f"Error from LLM: {llm_response}\n"
    else:
        insights_content += llm_response

    with open('/Users/ricc/git/gemini-cli-demos/demos/research-interest-in-public-repo/output/LLM_INSIGHTS.md', 'w') as f:
        f.write(insights_content)

    print("Successfully generated output/LLM_INSIGHTS.md with LLM insights.")

if __name__ == "__main__":
    generate_llm_insights()