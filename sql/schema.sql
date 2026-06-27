DROP TABLE IF EXISTS products;

CREATE TABLE products (
    sku_id INT PRIMARY KEY,
    category TEXT,
    name TEXT,
    mrp NUMERIC(10,2),
    discount NUMERIC(5,2),
    available_quantity INT,
    selling_price NUMERIC(10,2),
    weight INT,
    out_of_stock BOOLEAN,
    quantity INT,
    revenue NUMERIC(12,2),
    inventory_value NUMERIC(12,2),
    price_per_gram NUMERIC(12,4),
    estimated_profit NUMERIC(12,2),
    weight_category TEXT,
    city TEXT,
    state TEXT,
    region TEXT,
    latitude NUMERIC(9,4),
    longitude NUMERIC(9,4),
    warehouse TEXT,
    reorder_level INT,
    stock_status TEXT,
    revenue_band TEXT
);
