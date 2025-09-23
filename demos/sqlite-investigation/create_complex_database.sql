-- Copyright 2025 Google LLC
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may not- use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
--     http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.

PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;

-- Customers Table
CREATE TABLE customers (
  id INTEGER PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  address TEXT,
  signup_date TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Products Table
CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT,
  price REAL NOT NULL,
  stock_quantity INTEGER NOT NULL
);

-- Orders Table
CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  order_date TEXT DEFAULT CURRENT_TIMESTAMP,
  total_amount REAL NOT NULL,
  FOREIGN KEY(customer_id) REFERENCES customers(id)
);

-- Order Items Table
CREATE TABLE order_items (
  id INTEGER PRIMARY KEY,
  order_id INTEGER,
  product_id INTEGER,
  quantity INTEGER NOT NULL,
  price_per_unit REAL NOT NULL,
  FOREIGN KEY(order_id) REFERENCES orders(id),
  FOREIGN KEY(product_id) REFERENCES products(id)
);

-- Sample Data
INSERT INTO customers (id, first_name, last_name, email, address) VALUES
(1, 'John', 'Doe', 'john.doe@example.com', '123 Main St, Anytown, USA'),
(2, 'Jane', 'Smith', 'jane.smith@example.com', '456 Oak Ave, Otherville, USA');

INSERT INTO products (id, name, description, price, stock_quantity) VALUES
(1, 'Laptop', 'A high-performance laptop', 1200.00, 50),
(2, 'Mouse', 'A wireless optical mouse', 25.00, 200),
(3, 'Keyboard', 'A mechanical keyboard', 75.00, 150);

INSERT INTO orders (id, customer_id, total_amount) VALUES
(1, 1, 1225.00),
(2, 2, 100.00);

INSERT INTO order_items (order_id, product_id, quantity, price_per_unit) VALUES
(1, 1, 1, 1200.00),
(1, 2, 1, 25.00),
(2, 2, 2, 25.00),
(2, 3, 1, 75.00);

COMMIT;
