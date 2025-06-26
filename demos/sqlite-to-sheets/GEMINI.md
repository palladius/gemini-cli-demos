## Database creation script

I have a script to generate sqlite file in this folder.

## Further ideas

For each, make sure they're marked in README.md as done or todo. Use it as progress status.

1. [x] Create a `justfile` to create it.
2. [x] Create, for each table, a CSV containing all the fields out/TABLENAME.csv
3. [x] Move all CSVs as tab of a new Google Spreadsheet (1 table per tab)
   1. Have a `.env` file with ENV vars you want me to populate and give me instructions for things to do in the browser.

All things you produce and could be reproduced differently should be in `output/`,
except for `justfile` which i need here.

## Notes

* > one small nit: there's an empty sheet before the 3 you created: either you delete it you add a synopsis of what created this, what script, in which comptuer and
  PATH so if iland in this Trix i can always go back to the code that generated it. Use you fantasy.

* > one nest tip: the schema for the table (in row 1s) make it bold. And if the column is a key, make its name also underscored. Make foreign keys ITALIC instead.
