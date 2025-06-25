## Database creation script

Create a low-dependencies scripts (eg bash?) to generate a sqlite file.
This sqlite file should have a good schema (3-4 tables) and a few lines.
It's important that there are foreign keys connecting those tables, like for example:
- Events
- People
- Subscriptions (people to events)

Maybe the events can be recurring, which would need a 4th table? You choose, I dont care as long as the script consistently populates a sqlite file.

## Further ideas

* Create, for each table, a CSV containing all the fields out/TABLENAME.csv
* Move all CSVs as tab of a new Google Spreadsheet (1 table per tab)
