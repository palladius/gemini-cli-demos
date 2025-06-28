
import json
import csv

with open('data/stackoverflow/questions.json', 'r') as f:
    data = json.load(f)

with open('output/stackoverflow.csv', 'w', newline='') as f_csv:
    csv_writer = csv.writer(f_csv)
    csv_writer.writerow(['Question ID', 'Title', 'Tags', 'Answer Count', 'Score', 'Link'])

    for item in data['items']:
        csv_writer.writerow([
            item['question_id'],
            item['title'],
            ', '.join(item['tags']),
            item['answer_count'],
            item['score'],
            item['link']
        ])

print("Successfully created output/stackoverflow.csv")
