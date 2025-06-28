import json
import csv
from datetime import datetime
import yaml

with open('data/github/issues.json', 'r') as f:
    issues = json.load(f)

with open('data/googlers.yaml', 'r') as f:
    googlers = yaml.safe_load(f)
    googler_usernames = [g['username'] for g in googlers]

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
    # This function is a placeholder and does not perform actual translation.
    # It simply returns the original title.
    return title

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
        
        # Add Googler emoji if author is a Googler
        if issue.get('author') and issue['author'].get('login') in googler_usernames:
            title = f"🧢 {title}"

        truncated_title = (title[:61] + '...') if len(title) > 64 else title
        display_upvotes = str(upvotes) if upvotes > 0 else ''
        f_md.write(f'| {sentiment} | [{truncated_title}](https://github.com/google-gemini/gemini-cli/issues/{issue_number}) | {display_upvotes} |\n')

    f_md.write('\n## Top 20 Issues by Upvotes\n\n')
    f_md.write('| Sentiment | Title | Upvotes |\n')
    f_md.write('|---|---|---|\n')
    issues.sort(key=lambda x: get_upvotes(x['reactionGroups']), reverse=True)
    for issue in issues[:20]:
        issue_number = issue['number']
        title = translate_title(issue['title'])
        upvotes = get_upvotes(issue['reactionGroups'])
        sentiment = get_sentiment_emoji(title, issue['body'])

        # Add Googler emoji if author is a Googler
        if issue.get('author') and issue['author'].get('login') in googler_usernames:
            title = f"🧢 {title}"

        truncated_title = (title[:61] + '...') if len(title) > 64 else title
        display_upvotes = str(upvotes) if upvotes > 0 else ''
        f_md.write(f'| {sentiment} | [{truncated_title}](https://github.com/google-gemini/gemini-cli/issues/{issue_number}) | {display_upvotes} |\n')

    f_md.write('\n## Top 20 Issues by Comments\n\n')
    f_md.write('| Sentiment | Title | Comments |\n')
    f_md.write('|---|---|---|\n')
    issues.sort(key=lambda x: len(x['comments']), reverse=True)
    for issue in issues[:20]:
        issue_number = issue['number']
        title = translate_title(issue['title'])
        comments_count = len(issue['comments'])
        sentiment = get_sentiment_emoji(title, issue['body'])

        # Add Googler emoji if author is a Googler
        if issue.get('author') and issue['author'].get('login') in googler_usernames:
            title = f"🧢 {title}"

        truncated_title = (title[:61] + '...') if len(title) > 64 else title
        display_comments_count = str(comments_count) if comments_count > 0 else ''
        f_md.write(f'| {sentiment} | [{truncated_title}](https://github.com/google-gemini/gemini-cli/issues/{issue_number}) | {display_comments_count} |\n')

print("Successfully created output/issues.csv and output/issues.md")