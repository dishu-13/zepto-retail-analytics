# Power BI Dashboard Plan

I used Power BI to present the analysis in four simple pages.

## Page 1: Executive Dashboard

Main KPIs:
- Total Revenue
- Inventory Value
- Total Products
- Out of Stock Products

Useful visuals:
- Revenue by Category
- Out of Stock Products by Category
- Revenue Contribution %

## Page 2: Category Dashboard

Useful visuals:
- Revenue by Category
- Inventory Value by Category
- Average Discount by Category
- Product Count by Category

## Page 3: Product Dashboard

Useful visuals:
- Top 10 Products by Revenue
- Highest Discount Products
- Price Per Gram Analysis
- Weight Category Split

## Page 4: Inventory Dashboard

Useful visuals:
- Out of Stock Analysis
- Low Stock Products
- Inventory Risk by Category
- Reorder Suggestions

## DAX Measures

```DAX
Total Revenue = SUM(products[revenue])
```

```DAX
Inventory Value = SUM(products[inventory_value])
```

```DAX
Average Discount = AVERAGE(products[discount])
```

```DAX
Out of Stock Products =
CALCULATE(
    COUNTROWS(products),
    products[out_of_stock] = TRUE()
)
```
