PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT);
INSERT INTO users VALUES(1,'Alice','alice@example.com');
INSERT INTO users VALUES(2,'Bob','bob@example.com');
INSERT INTO users VALUES(3,'Susan','sue@example.com');
INSERT INTO users VALUES(4,'Richard','rich@example.com');
INSERT INTO users VALUES(5,'Esther','esther@example.com');
INSERT INTO users VALUES(6,'Francesco','checco@example.com');
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
