# Updated Database Schema and E/R Diagram

Here is the updated schema for the `events_and_people.sqlite` database, including the new `talks` and `event_talks` tables.

## SQL Schema

```sql
CREATE TABLE events (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  location TEXT,
  date TEXT
);
CREATE TABLE people (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  surname TEXT,
  email TEXT UNIQUE
);
CREATE TABLE subscriptions (
  person_id INTEGER,
  event_id INTEGER,
  FOREIGN KEY(person_id) REFERENCES people(id),
  FOREIGN KEY(event_id) REFERENCES events(id),
  PRIMARY KEY (person_id, event_id)
);
CREATE TABLE talks (id INTEGER PRIMARY KEY, title TEXT NOT NULL, abstract TEXT, person_id INTEGER, FOREIGN KEY(person_id) REFERENCES people(id));
CREATE TABLE event_talks (event_id INTEGER, talk_id INTEGER, FOREIGN KEY(event_id) REFERENCES events(id), FOREIGN KEY(talk_id) REFERENCES talks(id), PRIMARY KEY (event_id, talk_id));
```

## E/R Diagram (Mermaid)

The new tables (`talks` and `event_talks`) are highlighted in red.

```mermaid
erDiagram
    people {
        int id PK
        string name
        string surname
        string email
    }
    events {
        int id PK
        string name
        string location
        string date
    }
    subscriptions {
        int person_id FK
        int event_id FK
    }
    talks {
        int id PK
        string title
        string abstract
        int person_id FK
    }
    event_talks {
        int event_id FK
        int talk_id FK
    }

    people ||--o{ subscriptions : "subscribes to"
    events ||--o{ subscriptions : "is subscribed by"
    people ||--o{ talks : "gives"
    events ||--o{ event_talks : "has"
    talks ||--o{ event_talks : "is part of"

    classDef new_table fill:#f99,stroke:#333,stroke-width:2px;
    class talks,event_talks new_table

```