# Zepto Retail Intelligence & Inventory Analytics Platform

This is my end-to-end Data Analyst portfolio project using a Zepto retail inventory dataset.

I built this project to show the complete workflow of a data analyst:

1. Collect raw data
2. Clean it using Python
3. Store it in PostgreSQL
4. Analyze it using SQL
5. Build a Power BI dashboard plan
6. Create a simple Streamlit web app
7. Write business recommendations

The project is simple on purpose. I wanted it to be easy to explain in interviews and still show real business thinking.

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQL
- Power BI
- Streamlit
- Docker
- GitHub

## Project Architecture

```text
CSV Dataset
    -> Python ETL
    -> PostgreSQL Database
    -> SQL Analysis
    -> Power BI Dashboard
    -> Streamlit Web App
    -> Business Recommendations
```

## Folder Structure

```text
zepto-retail-analytics/
|-- data/
|   |-- raw/
|   |   |-- zepto.csv
|   |-- processed/
|       |-- zepto_cleaned.csv
|-- notebooks/
|   |-- 01_eda.ipynb
|-- sql/
|   |-- schema.sql
|   |-- analysis_queries.sql
|   |-- load_processed_csv.sql
|-- dashboard/
|   |-- powerbi_notes.md
|-- streamlit/
|   |-- app.py
|-- screenshots/
|-- business_recommendations.md
|-- PROJECT_REPORT.md
|-- docker-compose.yml
|-- etl.py
|-- requirements.txt
|-- README.md
```

## Dataset

The raw dataset contains product-level inventory data from Zepto.

Main columns in the raw file:

- `Category`
- `name`
- `mrp`
- `discountPercent`
- `availableQuantity`
- `discountedSellingPrice`
- `weightInGms`
- `outOfStock`
- `quantity`

The price columns in the raw dataset are stored in paise. I converted them into rupees during data cleaning.

## Data Cleaning

I cleaned the data using Python and Pandas.

Cleaning steps:

1. Removed duplicate rows
2. Removed products where MRP or selling price was zero
3. Converted MRP from paise to rupees
4. Converted selling price from paise to rupees
5. Created revenue column
6. Created inventory value column
7. Created price per gram column
8. Created weight category column
9. Added synthetic city, region, warehouse, latitude, and longitude fields for dashboard practice

New columns created:

```text
revenue = selling_price * available_quantity
inventory_value = mrp * available_quantity
price_per_gram = selling_price / weight
weight_category = Small / Medium / Large
```

Note: The original CSV does not contain location fields. I added synthetic location and warehouse columns so the Streamlit dashboard can show map and regional analysis.

## How To Run

### 1. Install libraries

```bash
pip install -r requirements.txt
```

### 2. Create cleaned CSV

```bash
python etl.py
```

This creates:

```text
data/processed/zepto_cleaned.csv
```

### 3. Start PostgreSQL using Docker

```bash
docker compose up -d
```

### 4. Load data into PostgreSQL

```bash
python etl.py --load-db
```

This creates a PostgreSQL table:

```text
products
```

### 5. Run SQL analysis

Open this file in pgAdmin, DBeaver, or another PostgreSQL client:

```text
sql/analysis_queries.sql
```

### 6. Run Streamlit app

```bash
streamlit run streamlit/app.py
```

## SQL Questions Answered

- What is the total revenue?
- Which categories generate the highest revenue?
- What are the top 10 products by revenue?
- What is each category's revenue contribution?
- Which categories have the most out-of-stock products?
- Which products have the highest discount?
- Which products give the best value by price per gram?
- Which products need reorder attention?

## Power BI Dashboard Plan

I planned four dashboard pages:

1. Executive Dashboard
2. Category Dashboard
3. Product Dashboard
4. Inventory Dashboard

Main KPIs:

- Total Revenue
- Inventory Value
- Total Products
- Out of Stock Products
- Average Discount

## Streamlit App Features

The Streamlit app includes:

- Revenue dashboard
- Inventory dashboard
- Executive dashboard
- Location map dashboard
- Category filter
- Region filter
- City filter
- Stock status filter
- Discount range filter
- Product search
- Download cleaned report button

## Business Recommendations

Based on the analysis, my recommendations are:

1. Increase stock for high-revenue categories with out-of-stock products.
2. Review high-discount products because they may reduce profit margin.
3. Promote products with low price per gram as value-for-money items.
4. Monitor inventory value by category to avoid overstocking.
5. Create reorder alerts for products with low available quantity.

## What I Learned

This project helped me practice:

- Data cleaning with Pandas
- PostgreSQL table design
- SQL business analysis
- Dashboard planning
- Streamlit app development
- Turning data into business recommendations

## Project Status

Completed as a portfolio project. Power BI screenshots can be added inside the `screenshots/` folder after creating the dashboard.
