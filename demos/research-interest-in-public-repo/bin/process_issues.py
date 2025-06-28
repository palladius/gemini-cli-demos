import json
import csv
import re
from datetime import datetime
import subprocess

def get_sentiment_emoji(title, body):
    title_lower = title.lower()
    body_lower = body.lower() if body else ""
    if 'bug' in title_lower or 'error' in title_lower or 'fail' in title_lower:
        return '🐛'
    if 'feature' in title_lower or 'request' in title_lower:
        return '✨'
    if 'suggestion' in title_lower or 'idea' in title_lower:
        return '🤔'
    if 'question' in title_lower or 'how to' in title_lower:
        return '❓'
    # Simple sentiment analysis based on keywords
    positive_words = ['good', 'great', 'awesome', 'love', 'like']
    negative_words = ['bad', 'hate', 'dislike', 'problem']
    if any(word in body_lower for word in positive_words):
        return '👍'
    if any(word in body_lower for word in negative_words):
        return '👎'
    if '```' in body_lower or '`' in title_lower:
        return '💻'
    return '📝' # Default to document emoji

def get_upvotes(reaction_groups):
    for group in reaction_groups:
        if group['content'] == 'THUMBS_UP':
            return group['users']['totalCount']
    return 0

def translate_title(title):
    if not re.match(r'^[\x00-\x7F]+$', title):
        try:
            # This is a placeholder for a real translation API call
            # In a real scenario, you would use a library like googletrans
            # For this example, we'll just prepend "(Translated) "
            return f"(Translated) {title}"
        except Exception as e:
            print(f"Error translating title: {e}")
            return title
    return title

with open('data/github/issues.json', 'r') as f:
    issues = json.load(f)

# Sort issues by creation date DESC
issues.sort(key=lambda x: datetime.strptime(x['createdAt'], '%Y-%m-%dT%H:%M:%SZ'), reverse=True)

with open('output/issues.csv', 'w', newline='') as f_csv, open('output/issues.md', 'w') as f_md:
    csv_writer = csv.writer(f_csv)
    csv_writer.writerow(['ID', 'Title', 'Upvotes', 'Sentiment', 'Synopsis'])
    
    for issue in issues:
        issue_id = issue['id']
        title = translate_title(issue['title'])
        upvotes = get_upvotes(issue['reactionGroups'])
        sentiment = get_sentiment_emoji(title, issue['body'])
        synopsis = (issue['body'] or '').replace('\n', ' ').replace('\r', ' ')[:160]

        csv_writer.writerow([issue_id, title, upvotes, sentiment, synopsis])

    f_md.write('# GitHub Issues\n\n')
    f_md.write('## Latest 50 Issues\n\n')
    f_md.write('| Sentiment | Title | Upvotes |\n')
    f_md.write('|---|---|---|\n')
    for issue in issues[:50]:
        issue_number = issue['number']
        title = translate_title(issue['title'])
        upvotes = get_upvotes(issue['reactionGroups'])
        sentiment = get_sentiment_emoji(title, issue['body'])
        truncated_title = (title[:61] + '...') if len(title) > 64 else title
        f_md.write(f'| {sentiment} | [{truncated_title}](https://github.com/google-gemini/gemini-cli/issues/{issue_number}) | {upvotes} |\n')

    f_md.write('\n## Top 20 Issues by Upvotes\n\n')
    f_md.write('| Sentiment | Title | Upvotes |\n')
    f_md.write('|---|---|---|\n')
    issues.sort(key=lambda x: get_upvotes(x['reactionGroups']), reverse=True)
    for issue in issues[:20]:
        issue_number = issue['number']
        title = translate_title(issue['title'])
        upvotes = get_upvotes(issue['reactionGroups'])
        sentiment = get_sentiment_emoji(title, issue['body'])
        truncated_title = (title[:61] + '...') if len(title) > 64 else title
        f_md.write(f'| {sentiment} | [{truncated_title}](https://github.com/google-gemini/gemini-cli/issues/{issue_number}) | {upvotes} |\n')

print("Successfully created output/issues.csv and output/issues.md")