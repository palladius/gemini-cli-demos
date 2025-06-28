#!/usr/bin/env python3
import csv
import yaml
import json
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure the Gemini API key
# It's recommended to load this from an environment variable for security
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if GEMINI_API_KEY:
    print("Gemini API key found.")
    genai.configure(api_key=GEMINI_API_KEY)
else:
    print("Gemini API key not found. Please set the GEMINI_API_KEY environment variable and try again.")
    exit(1) # Exit if API key is not found

def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating content: {e}"

def summarize_issue(issue_title, issue_body):
    prompt = f"""Summarize the following GitHub issue. Focus on the core problem or feature request.
Title: {issue_title}
Body: {issue_body}
Summary:"""
    return get_gemini_response(prompt)

def identify_duplicates(issue1_title, issue1_summary, issue2_title, issue2_summary):
    prompt = f"""Are the following two GitHub issues duplicates or highly similar?
Issue 1 Title: {issue1_title}
Issue 1 Summary: {issue1_summary}

Issue 2 Title: {issue2_title}
Issue 2 Summary: {issue2_summary}

Respond with "YES" if they are duplicates or highly similar, and "NO" otherwise. If YES, explain why briefly.
"""
    return get_gemini_response(prompt)

def generate_llm_insights():
    insights_content = "# LLM-Generated Insights\n\n"

    # Load issues data
    issues_data = []
    try:
        with open('/Users/ricc/git/gemini-cli-demos/demos/research-interest-in-public-repo/output/issues.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                issues_data.append(row)
    except FileNotFoundError:
        insights_content += "Error: issues.csv not found. Please run process_issues.py first.\n"
        with open('/Users/ricc/git/gemini-cli-demos/demos/research-interest-in-public-repo/output/INSIGHTS.md', 'w') as f:
            f.write(insights_content)
        return

    # Generate summaries for each issue
    print("Generating LLM summaries for issues...")
    summarized_issues = []
    for i, issue in enumerate(issues_data):
        print(f"  Summarizing issue {i+1}/{len(issues_data)}: {issue['Title']}")
        # Assuming 'Synopsis' from issues.csv is a good starting point for issue body
        # For a more accurate summary, you might need to fetch the full issue body from GitHub API
        summary = summarize_issue(issue['Title'], issue['Synopsis'])
        summarized_issues.append({
            'ID': issue['ID'],
            'Title': issue['Title'],
            'Synopsis': issue['Synopsis'],
            'Summary': summary
        })
        insights_content += f"## Issue {issue['ID']}: {issue['Title']}\n"
        insights_content += f"**LLM Summary:** {summary}\n\n"

    # Identify potential duplicates
    print("Identifying potential duplicate issues...")
    insights_content += "## Potential Duplicate Issues (LLM-Identified)\n\n"
    found_duplicates = False
    total_comparisons = (len(summarized_issues) * (len(summarized_issues) - 1)) // 2
    comparison_count = 0
    for i in range(len(summarized_issues)):
        for j in range(i + 1, len(summarized_issues)):
            comparison_count += 1
            print(f"  Comparing issue {summarized_issues[i]['ID']} with {summarized_issues[j]['ID']} ({comparison_count}/{total_comparisons})")
            issue1 = summarized_issues[i]
            issue2 = summarized_issues[j]
            duplicate_check = identify_duplicates(
                issue1['Title'], issue1['Summary'],
                issue2['Title'], issue2['Summary']
            )
            if "YES" in duplicate_check.upper():
                found_duplicates = True
                insights_content += f"- Issues {issue1['ID']} and {issue2['ID']} are potential duplicates:\n"
                insights_content += f"  - Issue 1: [{issue1['Title']}](https://github.com/google-gemini/gemini-cli/issues/{issue1['ID']})\n"
                insights_content += f"  - Issue 2: [{issue2['Title']}](https://github.com/google-gemini/gemini-cli/issues/{issue2['ID']})\n"
                insights_content += f"  **Reason:** {duplicate_check}\n\n"

    if not found_duplicates:
        insights_content += "No LLM-identified duplicate issues found.\n\n"

    with open('/Users/ricc/git/gemini-cli-demos/demos/research-interest-in-public-repo/output/INSIGHTS.md', 'w') as f:
        f.write(insights_content)

    print("Successfully generated output/INSIGHTS.md with LLM insights.")

if __name__ == "__main__":
    generate_llm_insights()
