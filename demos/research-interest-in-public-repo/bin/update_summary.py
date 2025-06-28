
import csv
import yaml
import re

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

def get_reddit_sentiment(title):
    title_lower = title.lower()
    if "good" in title_lower or "awesome" in title_lower or "great" in title_lower:
        return "Positive 👍"
    elif "bad" in title_lower or "mistake" in title_lower or "problem" in title_lower:
        return "Negative 👎"
    else:
        return "Neutral 📝"

# Issues statistics
issue_count = 0
positive_issues = 0
negative_issues = 0
neutral_issues = 0
with open('output/issues.csv', 'r') as f_csv:
    reader = csv.reader(f_csv)
    next(reader)  # Skip header
    for row in reader:
        issue_count += 1
        sentiment = row[3] # Assuming sentiment is the 4th column (index 3)
        if sentiment == '👍' or sentiment == '✨':
            positive_issues += 1
        elif sentiment == '👎' or sentiment == '🐛':
            negative_issues += 1
        else:
            neutral_issues += 1

# Stack Overflow statistics
stackoverflow_count = 0
with open('output/stackoverflow.csv', 'r') as f_csv:
    reader = csv.reader(f_csv)
    next(reader)  # Skip header
    for row in reader:
        stackoverflow_count += 1

# Reddit statistics
reddit_count = 0
positive_reddit = 0
negative_reddit = 0
neutral_reddit = 0
with open('data/reddit/posts.yaml', 'r') as f:
    reddit_posts = yaml.safe_load(f)
    for post in reddit_posts:
        reddit_count += 1
        sentiment = get_reddit_sentiment(post['title'])
        if sentiment == 'Positive 👍':
            positive_reddit += 1
        elif sentiment == 'Negative 👎':
            negative_reddit += 1
        else:
            neutral_reddit += 1

# Read the README.md template
readme_template = """
# Gemini CLI Public Interest Monitoring Summary

This document provides a summary of the public interest in the Gemini CLI, gathered from various sources.

## GitHub Issues

- [View GitHub Issues (Latest 50)](./issues.md#latest-50-issues)
- [View GitHub Issues (Top 20 by Upvotes)](./issues.md#top-20-issues-by-upvotes)

**Statistics:**
- Total Issues: {issue_count}
- Positive Sentiment Issues: {positive_issues}
- Negative Sentiment Issues: {negative_issues}

## Stack Overflow Questions

- [View Stack Overflow Questions](./stackoverflow.csv)

**Statistics:**
- Total Questions: {stackoverflow_count}

## Reddit Posts

- [View Reddit Posts](./reddit.md)

**Statistics:**
- Total Posts: {reddit_count}
- Positive Sentiment Posts: {positive_reddit}
- Negative Sentiment Posts: {negative_reddit}

## Sentiment Analysis Pie Chart

(Placeholder for a pie chart showing the distribution of sentiment across issues, e.g., Red for Negative, Green for Positive, Blue for Neutral/Code-related)

```
[Pie Chart Image Here]
```
"""

# Format the README content with the collected statistics
readme_content = readme_template.format(
    issue_count=issue_count,
    positive_issues=positive_issues,
    negative_issues=negative_issues,
    stackoverflow_count=stackoverflow_count,
    reddit_count=reddit_count,
    positive_reddit=positive_reddit,
    negative_reddit=negative_reddit
)

# Write the updated README.md
with open('output/README.md', 'w') as f:
    f.write(readme_content)

print("Successfully updated output/README.md with statistics.")
