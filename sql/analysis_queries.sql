-- 1. Total business KPIs
SELECT
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(inventory_value), 2) AS total_inventory_value,
    COUNT(*) AS total_products,
    SUM(CASE WHEN out_of_stock THEN 1 ELSE 0 END) AS out_of_stock_products
FROM products;

-- 2. Top revenue categories
SELECT
    category,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM products
GROUP BY category
ORDER BY total_revenue DESC;

-- 3. Top 10 products by revenue
SELECT
    name,
    category,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM products
GROUP BY name, category
ORDER BY total_revenue DESC
LIMIT 10;

-- 4. Category contribution percentage
SELECT
    category,
    ROUND(SUM(revenue) * 100.0 / (SELECT SUM(revenue) FROM products), 2) AS revenue_contribution_percent
FROM products
GROUP BY category
ORDER BY revenue_contribution_percent DESC;

-- 5. Inventory risk by category
SELECT
    category,
    COUNT(*) AS out_of_stock_products
FROM products
WHERE out_of_stock = TRUE
GROUP BY category
ORDER BY out_of_stock_products DESC;

-- 6. Revenue ranking inside each category
SELECT
    name,
    category,
    revenue,
    RANK() OVER (
        PARTITION BY category
        ORDER BY revenue DESC
    ) AS revenue_rank
FROM products;

-- 7. Running revenue by category
SELECT
    category,
    name,
    revenue,
    SUM(revenue) OVER (
        PARTITION BY category
        ORDER BY revenue DESC
    ) AS running_revenue
FROM products;

-- 8. Best value products by price per gram
SELECT
    name,
    category,
    selling_price,
    weight,
    ROUND(price_per_gram, 4) AS price_per_gram
FROM products
WHERE weight > 0
ORDER BY price_per_gram ASC
LIMIT 20;

-- 9. High discount products
SELECT
    name,
    category,
    mrp,
    selling_price,
    discount
FROM products
ORDER BY discount DESC
LIMIT 20;

-- 10. Reorder suggestion
SELECT
    category,
    name,
    available_stock.out_of_stock,
    available_stock.available_quantity,
    CASE
        WHEN available_stock.out_of_stock = TRUE THEN 'Urgent reorder'
        WHEN available_stock.available_quantity <= 3 THEN 'Low stock'
        ELSE 'Healthy stock'
    END AS reorder_status
FROM (
    SELECT
        category,
        name,
        out_of_stock,
        available_quantity
    FROM products
) AS available_stock
ORDER BY reorder_status, category;
