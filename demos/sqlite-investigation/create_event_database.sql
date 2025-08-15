-- Copyright 2025 Google LLC
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
--     http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.


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
  surname TEXT,
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

INSERT INTO people (id, name, surname, email) VALUES
(1, 'Alice', 'Smith', 'alice@example.com'),
(2, 'Bob', 'Jones', 'bob@example.com');

INSERT INTO subscriptions (person_id, event_id) VALUES
(1, 1),
(1, 2),
(2, 2);

COMMIT;
