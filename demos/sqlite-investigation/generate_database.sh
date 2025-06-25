#!/bin/bash
# This script generates the events_and_people.sqlite database.

# Remove the old database file if it exists
rm -f events_and_people.sqlite

# Create the new database from the SQL script
sqlite3 events_and_people.sqlite < create_event_database.sql

echo "Database 'events_and_people.sqlite' created successfully."
