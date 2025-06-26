
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

-- Events Table
CREATE TABLE events (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  location TEXT,
  date TEXT
);

-- People Table
CREATE TABLE people (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE
);

-- Subscriptions Table
CREATE TABLE subscriptions (
  person_id INTEGER,
  event_id INTEGER,
  FOREIGN KEY(person_id) REFERENCES people(id),
  FOREIGN KEY(event_id) REFERENCES events(id),
  PRIMARY KEY (person_id, event_id)
);

-- Sample Data
INSERT INTO events (id, name, location, date) VALUES
(1, 'Tech Conference 2025', 'Virtual', '2025-10-15'),
(2, 'Local Hackathon', 'City Library', '2025-11-01');

INSERT INTO people (id, name, email) VALUES
(1, 'Alice', 'alice@example.com'),
(2, 'Bob', 'bob@example.com');

INSERT INTO subscriptions (person_id, event_id) VALUES
(1, 1),
(1, 2),
(2, 2);

COMMIT;
