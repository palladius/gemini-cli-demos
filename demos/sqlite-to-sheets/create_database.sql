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
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT);
INSERT INTO users VALUES(1,'Alice','alice@example.com');
INSERT INTO users VALUES(2,'Bob','bob@example.com');
INSERT INTO users VALUES(3,'Susan','sue@example.com');
INSERT INTO users VALUES(4,'Richard','rich@example.com');
INSERT INTO users VALUES(5,'Esther','esther@example.com');
INSERT INTO users VALUES(6,'Francesco','checco@example.com');
INSERT INTO users VALUES(7,'Riccardo','ricc@example.com');
CREATE TABLE products (sku TEXT PRIMARY KEY, description TEXT, price REAL);
INSERT INTO products VALUES('WDG001','Magic Widget',19.98999999999999843);
INSERT INTO products VALUES('RIC042','HHTTG Book',41.99000000000000198);
CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  product_sku TEXT,
  FOREIGN KEY(user_id) REFERENCES users(id),
  FOREIGN KEY(product_sku) REFERENCES products(sku)
);
INSERT INTO orders VALUES(1,1,'WDG001');
INSERT INTO orders VALUES(2,2,'RIC042');
INSERT INTO orders VALUES(3,1,'RIC042');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('orders',3);
COMMIT;
