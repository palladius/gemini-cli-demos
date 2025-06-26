#!/bin/bash

# Ensure the output directory exists
mkdir -p output

# Export tables to CSV
sqlite3 -header -csv people_and_orders.sqlite "select * from users;" > output/users.csv
sqlite3 -header -csv people_and_orders.sqlite "select * from products;" > output/products.csv
sqlite3 -header -csv people_and_orders.sqlite "select * from orders;" > output/orders.csv

echo "CSV files updated successfully in the 'output' directory."
