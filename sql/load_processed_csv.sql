-- Use this only if you want to load the cleaned CSV manually from PostgreSQL.
-- Update the file path before running this command.

\copy products(
    sku_id,
    category,
    name,
    mrp,
    discount,
    available_quantity,
    selling_price,
    weight,
    out_of_stock,
    quantity,
    revenue,
    inventory_value,
    price_per_gram,
    estimated_profit,
    weight_category,
    city,
    state,
    region,
    latitude,
    longitude,
    warehouse,
    reorder_level,
    stock_status,
    revenue_band
)
FROM 'C:/Users/dishu/Downloads/data anal/zepto-retail-analytics/data/processed/zepto_cleaned.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', QUOTE '"', ENCODING 'UTF8');
