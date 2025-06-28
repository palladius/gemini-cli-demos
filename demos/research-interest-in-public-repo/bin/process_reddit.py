
import yaml
import csv

# Sample sentiment analysis function (replace with actual LLM call if available)
def get_sentiment(title):
    title_lower = title.lower()
    if "good" in title_lower or "awesome" in title_lower or "great" in title_lower:
        return "Positive 👍"
    elif "bad" in title_lower or "mistake" in title_lower or "problem" in title_lower:
        return "Negative 👎"
    else:
        return "Neutral 📝"

with open('data/reddit/posts.yaml', 'r') as f:
    reddit_posts = yaml.safe_load(f)

with open('output/reddit.md', 'w') as f_md:
    f_md.write('# Reddit Posts\n\n')
    f_md.write('| Sentiment | Title | Subreddit | Permalink |\n')
    f_md.write('|---|---|---|---|\n')

    for i, post in enumerate(reddit_posts[:50]):
        title = post['title']
        subreddit = post['subreddit']
        sentiment = get_sentiment(title)
        permalink = post.get('permalink', '') # Get permalink, default to empty string
        if permalink:
            f_md.write(f'| {sentiment} | [{title}]({permalink}) | {subreddit} | [Link]({permalink}) |\n')
        else:
            f_md.write(f'| {sentiment} | {title} | {subreddit} | (Not available) |\n')

print("Successfully created output/reddit.md")
