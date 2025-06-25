CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  product_sku TEXT,
  FOREIGN KEY(user_id) REFERENCES users(id),
  FOREIGN KEY(product_sku) REFERENCES products(sku)
);

INSERT INTO orders (user_id, product_sku) VALUES (1, 'WDG001');
INSERT INTO orders (user_id, product_sku) VALUES (2, 'RIC042');
INSERT INTO orders (user_id, product_sku) VALUES (1, 'RIC042');
