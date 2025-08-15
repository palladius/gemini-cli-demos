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

import yaml
import csv

# Sample sentiment analysis function (replace with actual LLM call if available)
def get_sentiment(title):
    title_lower = title.lower()
    if "good" in title_lower or "awesome" in title_lower or "great" in title_lower:
        return "👍"
    elif "bad" in title_lower or "mistake" in title_lower or "problem" in title_lower:
        return "👎"
    else:
        return "📝" # Neutral sentiment emoji

with open('data/reddit/posts.yaml', 'r') as f:
    reddit_posts = yaml.safe_load(f)

with open('output/reddit.md', 'w') as f_md:
    f_md.write('# Reddit Posts\n\n')
    f_md.write('| Sentiment | Title | Subreddit |\n')
    f_md.write('|---|---|---|\n')

    for i, post in enumerate(reddit_posts[:50]):
        title = post['title']
        subreddit = post['subreddit']
        sentiment = get_sentiment(title)
        permalink = post.get('permalink', '') # Get permalink, default to empty string

        linked_title = f'[{title}]({permalink})' if permalink else title
        linked_subreddit = f'[{subreddit}](https://www.reddit.com/{subreddit}/)'

        f_md.write(f'| {sentiment} | {linked_title} | {linked_subreddit} |\n')

print("Successfully created output/reddit.md")