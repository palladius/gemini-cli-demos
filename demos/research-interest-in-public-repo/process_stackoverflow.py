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
