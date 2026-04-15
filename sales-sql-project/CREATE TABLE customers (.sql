CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name TEXT NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);