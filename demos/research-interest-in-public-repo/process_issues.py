
import json
import csv

with open('data/github/issues.json', 'r') as f:
    issues = json.load(f)

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

with open('output/issues.csv', 'w', newline='') as f_csv, open('output/issues.md', 'w') as f_md:
    csv_writer = csv.writer(f_csv)
    csv_writer.writerow(['ID', 'Title', 'Upvotes', 'Sentiment', 'Synopsis'])
    f_md.write('# GitHub Issues\n\n')

    # Sort issues by ID DESC
    issues.sort(key=lambda x: x['id'], reverse=True)

    for issue in issues:
        issue_id = issue['id']
        title = issue['title']
        upvotes = get_upvotes(issue['reactionGroups'])
        sentiment = get_sentiment_emoji(title, issue['body'])
        synopsis = (issue['body'] or '').replace('\n', ' ').replace('\r', ' ')[:160]

        csv_writer.writerow([issue_id, title, upvotes, sentiment, synopsis])

    # For markdown, sort by date (assuming id is a proxy for date) and take last 50
    issues.sort(key=lambda x: x['id'], reverse=True)
    for issue in issues[:50]:
        issue_id = issue['id']
        title = issue['title']
        upvotes = get_upvotes(issue['reactionGroups'])
        sentiment = get_sentiment_emoji(title, issue['body'])
        f_md.write(f"- **{title}** (ID: {issue_id}, Upvotes: {upvotes}, Sentiment: {sentiment})\n")

print("Successfully created output/issues.csv and output/issues.md")
