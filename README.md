# Zepto Retail Intelligence & Inventory Analytics Platform

This is my end-to-end Data Analyst portfolio project using a Zepto retail inventory dataset.

I made this project to show a complete analyst workflow:

1. Clean raw CSV data using Python
2. Create business columns like revenue and inventory value
3. Store and analyze the data using SQL
4. Build an interactive Streamlit dashboard
5. Share business insights in a simple project report

## Tech Stack

- Python
- Pandas
- SQL
- PostgreSQL
- Streamlit

## Project Flow

```text
Raw CSV
   -> Python Data Cleaning
   -> Cleaned CSV
   -> SQL Analysis
   -> Streamlit Dashboard
   -> Business Insights
```

## Final Folder Structure

```text
zepto-retail-analytics/
|-- data/
|   |-- raw/
|   |   |-- zepto.csv
|   |-- processed/
|       |-- zepto_cleaned.csv
|-- sample/
|   |-- dashboard screenshots and HR preview files
|-- sql/
|   |-- schema.sql
|   |-- analysis_queries.sql
|-- streamlit/
|   |-- app.py
|-- etl.py
|-- PROJECT_REPORT.md
|-- README.md
|-- requirements.txt
|-- docker-compose.yml
```

## What The Project Does

The project analyzes Zepto inventory and product data to answer questions like:

- Which categories generate the most revenue?
- Which products are top performers?
- Which products are out of stock?
- Which cities and regions perform better?
- Which products need reorder attention?
- Which products have high discount and high revenue?

## Dataset

The original CSV has:

- Product category
- Product name
- MRP
- Discount
- Selling price
- Available quantity
- Weight
- Out-of-stock flag

The original data did not have location fields, so I added synthetic city, state, region, warehouse, latitude, and longitude columns only for dashboard practice and map visuals.

## New Columns Created

```text
revenue = selling_price * available_quantity
inventory_value = mrp * available_quantity
price_per_gram = selling_price / weight
estimated_profit = selling_price * 18% * available_quantity
stock_status = Healthy Stock / Low Stock / Out of Stock
revenue_band = Low Revenue / Medium Revenue / High Revenue
```

## Dashboard Features

The Streamlit dashboard includes:

- Executive overview
- Revenue dashboard
- Inventory dashboard
- Location map dashboard
- Product search
- Category filter
- Region filter
- City filter
- Stock status filter
- Discount range filter
- KPI cards
- Bar chart, pie chart, treemap, scatter chart, line chart, box plot, and map

## How To Run

Install libraries:

```bash
pip install -r requirements.txt
```

Run data cleaning:

```bash
python etl.py
```

Run dashboard:

```bash
streamlit run streamlit/app.py
```

## SQL Files

The `sql/` folder contains:

- `schema.sql`: table structure
- `analysis_queries.sql`: business analysis queries

## HR Preview Samples

Open the `sample/` folder to quickly see professional screenshots and preview files:

- Dashboard pages
- Cleaned dataset preview
- SQL analysis file
- Python ETL file
- Project report
- Project architecture
- KPI summary

