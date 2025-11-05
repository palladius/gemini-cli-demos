
## Database Schema

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
CREATE TABLE talks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    abstract TEXT,
    person_id INTEGER,
    FOREIGN KEY(person_id) REFERENCES people(id)
);
CREATE TABLE event_talks (
    event_id INTEGER,
    talk_id INTEGER,
    FOREIGN KEY(event_id) REFERENCES events(id),
    FOREIGN KEY(talk_id) REFERENCES talks(id),
    PRIMARY KEY (event_id, talk_id)
);
```

## E/R Diagram (Mermaid)

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

    people ||--o{ subscriptions : "subscribes"
    events ||--o{ subscriptions : "has"
    people ||--o{ talks : "gives"
    events ||--o{ event_talks : "has"
    talks ||--o{ event_talks : "is part of"

    style talks fill:#ffcccc
    style event_talks fill:#ffcccc
```
