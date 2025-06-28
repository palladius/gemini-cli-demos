
import matplotlib.pyplot as plt
import json

with open('data/issue_sentiment.json', 'r') as f:
    sentiment_data = json.load(f)

labels = ['Positive', 'Negative', 'Neutral']
sizes = [sentiment_data['positive_issues'], sentiment_data['negative_issues'], sentiment_data['neutral_issues']]
colors = ['#4CAF50', '#F44336', '#2196F3'] # Green, Red, Blue

# Filter out zero values to avoid issues with pie chart plotting
filtered_sizes = []
filtered_labels = []
filtered_colors = []
for i, size in enumerate(sizes):
    if size > 0:
        filtered_sizes.append(size)
        filtered_labels.append(labels[i])
        filtered_colors.append(colors[i])

plt.figure(figsize=(8, 8))
plt.pie(filtered_sizes, labels=filtered_labels, colors=filtered_colors, autopct='%1.1f%%', startangle=140)
plt.title('GitHub Issue Sentiment Analysis')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('output/sentiment_pie_chart.png')
print("Successfully generated output/sentiment_pie_chart.png")
