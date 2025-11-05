# Script for WAD demo

As per go/ricc-gemini-cli:

```bash
# 00 - setup
./generate_database.sh
```

## PROMPTS - 3-slash-Ns separated

Launch gc: `giancarlo-permissive-nomcp` 

```markdown
What does this repo do?

Can u see a sqlite file here?
```
## double click on a specific DB (which we can easily recreate)

```markdown

Ok lets use events_and_people.sqlite which I’ve just generated with ./generate_database.sh . 
Can you look at this DB, show me the tables, their schemas, and if there are any events or people in it?

```


## Add a user and an event

```
I'm at an Hackathon event today with PSI SOftware Berlin

Ok, let’s now add a person (Riccardo Carlesso, make up a sample email for me) and I’m coming to this event (as per event link). Also make sure I attend (subscribe) this event. Also add presenters for the event (a chap named Daniel Strebel, I presume).

Finally add Jasper Bernhardt. 

Again fake email, as its just a demo.
```

## English -> SQL

Now execute a query to get the people attending the most events, with person and COUNT in the table sorted by count. Show me both the SQL query AND the result.

## Extend the DB

Now I want to extend the Database with a new concept. I want to add the fact that Riccardo is participating to the above event with a talk, called “Gemini CLI rocks”. A talk should have a title, an abstract, and a person id, and it can be linked in 1:many to an event, and I want you to both create the tables to make this happen and add this talk , and “attach” it to both the above event AND the Tech Conference 2025 to demonstrate the 1:many relationship. In the end, show me some SQL to demonstrate it.


## Wow moment

Now that we have more tables, help me create/update the “output/DEMO2.md” with the updated schema and the updated E/R diagram in mermaid, similarly to what you can see in output/OUTPUT.md .

If possible, color the new table(s) differently, like in RED.


# Cleanup

```bash
# 99 - cleanup - TODO just cleanup
rm output/DEMO2.md
```
