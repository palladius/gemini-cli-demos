import csv
import yaml
import json
from collections import defaultdict

def generate_insights():
    insights_content = "# Insights\n\n"

    # --- GitHub Issues Insights ---
    issues_data = []
    # Read issues.csv to get the issue number
    with open('output/issues.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            issues_data.append(row)

    # To get the issue number, I need to read the original issues.json
    # because issues.csv does not contain the issue number, only the ID.
    # Or, I can modify process_issues.py to include issue number in issues.csv
    # Let's modify process_issues.py to include issue number in issues.csv for consistency.
    # For now, I will read issues.json to get the number.
    github_issues_raw = []
    with open('data/github/issues.json', 'r') as f:
        github_issues_raw = json.load(f)

    # Create a mapping from issue ID to issue number
    issue_id_to_number = {issue['id']: issue['number'] for issue in github_issues_raw}

    insights_content += "## GitHub Issues: Potential Duplicates and Similarities\n\n"
    # Simple duplicate detection based on title similarity
    # This is a deterministic approach, not LLM-based semantic understanding
    title_groups = defaultdict(list)
    for issue in issues_data:
        # Normalize title for comparison (lowercase, remove non-alphanumeric)
        normalized_title = ' '.join(sorted(re.findall(r'\b\w+\b', issue['Title'].lower())))
        title_groups[normalized_title].append(issue)

    found_duplicates = False
    for normalized_title, group in title_groups.items():
        if len(group) > 1:
            found_duplicates = True
            insights_content += f"### Similar Issues (based on title keywords):\n"
            for issue in group:
                # Use the mapping to get the issue number
                issue_number = issue_id_to_number.get(issue['ID'], 'UNKNOWN')
                insights_content += f"- [{issue['Title']}](https://github.com/google-gemini/gemini-cli/issues/{issue_number})\n"
            insights_content += "\n"

    if not found_duplicates:
        insights_content += "No obvious duplicate or highly similar issues found based on title keywords.\n\n"

    # --- Stack Overflow Conversations Insights ---
    stackoverflow_data = []
    with open('output/stackoverflow.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stackoverflow_data.append(row)

    insights_content += "## Stack Overflow: Potential Duplicate or Related Questions\n\n"
    so_title_groups = defaultdict(list)
    for q in stackoverflow_data:
        normalized_title = ' '.join(sorted(re.findall(r'\b\w+\b', q['Title'].lower())))
        so_title_groups[normalized_title].append(q)

    found_so_duplicates = False
    for normalized_title, group in so_title_groups.items():
        if len(group) > 1:
            found_so_duplicates = True
            insights_content += f"### Similar Questions (based on title keywords):\n"
            for q in group:
                insights_content += f"- [{q['Title']}]({q['Link']})\n"
            insights_content += "\n"

    if not found_so_duplicates:
        insights_content += "No obvious duplicate or highly similar Stack Overflow questions found.\n\n"

    # --- Reddit Conversations Insights ---
    reddit_data = []
    with open('data/reddit/posts.yaml', 'r') as f:
        reddit_data = yaml.safe_load(f)

    insights_content += "## Reddit: Potential Duplicate or Related Conversations\n\n"
    reddit_title_groups = defaultdict(list)
    for p in reddit_data:
        normalized_title = ' '.join(sorted(re.findall(r'\b\w+\b', p['title'].lower())))
        reddit_title_groups[normalized_title].append(p)

    found_reddit_duplicates = False
    for normalized_title, group in reddit_title_groups.items():
        if len(group) > 1:
            found_reddit_duplicates = True
            insights_content += f"### Similar Conversations (based on title keywords):\n"
            for p in group:
                permalink = p.get('permalink', '')
                if permalink:
                    insights_content += f"- [{p['title']}]({permalink}) (Subreddit: {p['subreddit']})\n"
                else:
                    insights_content += f"- {p['title']} (Subreddit: {p['subreddit']}) (Permalink not available)\n"
            insights_content += "\n"

    if not found_reddit_duplicates:
        insights_content += "No obvious duplicate or highly similar Reddit conversations found.\n\n"

    with open('output/INSIGHTS.md', 'w') as f:
        f.write(insights_content)

    print("Successfully generated output/INSIGHTS.md")

if __name__ == "__main__":
    import re # Import re here to make it available in the function scope
    generate_insights()