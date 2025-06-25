#!/bin/bash
# This script generates the people_and_orders.sqlite database.

# Remove the old database file if it exists
rm -f people_and_orders.sqlite

# Create the new database from the SQL script
sqlite3 people_and_orders.sqlite < create_database.sql

echo "Database 'people_and_orders.sqlite' created successfully."
