#!/bin/bash
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

# This script generates the events_and_people.sqlite database.

# Remove the old database file if it exists
rm -f events_and_people.sqlite

# Create the new database from the SQL script
sqlite3 events_and_people.sqlite < create_event_database.sql

echo "Database 'events_and_people.sqlite' created successfully."
