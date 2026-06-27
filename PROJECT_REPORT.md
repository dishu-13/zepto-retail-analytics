# Project Report

## Project Title

Zepto Retail Intelligence & Inventory Analytics Platform

## Problem Statement

Retail and quick-commerce companies need to track product availability, pricing, discounts, and category-level revenue. In this project, I analyzed Zepto product inventory data to understand which categories and products are performing well and where inventory risk exists.

## Objective

The objective of this project is to build a complete data analyst workflow from raw CSV data to business recommendations.

## Tools Used

- Python and Pandas for data cleaning
- PostgreSQL for database storage
- SQL for business analysis
- Power BI for dashboard planning
- Streamlit for a simple web app
- Docker for running PostgreSQL locally

## Data Preparation

The raw dataset had product details such as category, product name, MRP, discount, selling price, available quantity, product weight, and stock status.

I cleaned the data by:

1. Removing duplicate rows
2. Removing invalid price rows
3. Converting prices from paise to rupees
4. Creating calculated columns for revenue, inventory value, and price per gram
5. Grouping products into weight categories

## Key Analysis Areas

- Revenue by category
- Top products by revenue
- Inventory value by category
- Out-of-stock products
- Discount analysis
- Price per gram analysis
- Reorder suggestions

## Business Impact

This project can help a retail team:

- Find high-revenue categories
- Identify products that need restocking
- Track overstocked inventory
- Review discount strategy
- Promote best-value products

## Interview Explanation

I can explain this project as:

"I built an end-to-end retail analytics project using Zepto inventory data. I cleaned the raw CSV using Python, created revenue and inventory metrics, loaded the data into PostgreSQL, wrote SQL queries for business analysis, planned a Power BI dashboard, and built a Streamlit app for quick product and inventory insights."

## Final Outcome

The final project includes cleaned data, SQL analysis, dashboard notes, a Streamlit app, and business recommendations. It is ready to upload to GitHub as a portfolio project.
