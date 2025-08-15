#!/usr/bin/env python3
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")
LLM_ISSUE_LIMIT = int(os.environ.get("LLM_ISSUE_LIMIT", 50))

if GEMINI_API_KEY:
    print("Gemini API key found.")
    genai.configure(api_key=GEMINI_API_KEY)
else:
    print("Gemini API key not found. Please set the GEMINI_API_KEY environment variable and try again.")
    exit(1) # Exit if API key is not found

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
        # Horrible hardcoded path
        with open('./data/github/issues.json', 'r') as f:
            issues_data = json.load(f)
    except FileNotFoundError:
        insights_content += "Error: data/github/issues.json not found. Please run process_issues.py first to fetch GitHub issues.\n"
        with open('./output/LLM_INSIGHTS.md', 'w') as f:
            f.write(insights_content)
        return

    print(f"Loaded {len(issues_data)} issues. Limiting to {LLM_ISSUE_LIMIT} for LLM processing. Preparing prompt for LLM...")

    # Construct the comprehensive prompt
    prompt_parts = [
        "You are an expert in analyzing GitHub issues. Your task is to summarize a list of issues and identify potential duplicates or highly similar issues. For each identified duplicate group, explain why they are considered duplicates and suggest a course of action.",
        "\n\nHere is the list of GitHub issues, each with a numeric ID (issue number), Title, and Body:",
        "\n\n---"
    ]

    for issue in issues_data[:LLM_ISSUE_LIMIT]:
        prompt_parts.append(f"ID: {issue['number']}\nTitle: {issue['title']}\nBody: {issue['body']}\n---")

    prompt_parts.append("""Your output should be in Markdown format, structured as follows:

## Issue Summaries
For each issue, provide a concise summary (2-3 sentences). Prepend each summary with the issue's numeric ID hyperlinked to its GitHub page (e.g., [2244](https://github.com/google-gemini/gemini-cli/issues/2244)).
If the issue appears to be a Feature Request, add a 💡 emoji before the ID. If it's a Bug, add a 🐛 emoji.
If the issue is specific to an Operating System (Windows, Linux, or Apple/macOS), prepend the line with the corresponding emoji (🪟 for Windows, 🐧 for Linux, 🍎 for Apple).

## Potential Duplicate Issues
List groups of issues that are duplicates or highly similar. For each group, provide:
- The numeric IDs and Titles of the issues in the group, with permalinks to their GitHub pages (e.g., [Title](https://github.com/google-gemini/gemini-cli/issues/ID)).
- A brief explanation of why they are duplicates/similar.
- A 'Course of Action:' bullet point suggesting how to handle them (e.g., 'Merge A into B', 'Close A as duplicate of B', 'Cross-reference A and B').

## General Insights and Course of Action
Provide any other general insights or recurring themes you notice, and suggest overall courses of action.""")

    full_prompt = "\n".join(prompt_parts)

    # Save the full prompt to .cache/
    cache_dir = './.cache'
    os.makedirs(cache_dir, exist_ok=True)
    prompt_cache_file = os.path.join(cache_dir, 'llm_prompt_for_insights.md')
    with open(prompt_cache_file, 'w') as f:
        f.write(full_prompt)
    print(f"Full prompt saved to {prompt_cache_file}")

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
