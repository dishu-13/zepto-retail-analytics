import sys

import pandas as pd


# Step 1: Load raw data
df = pd.read_csv("data/raw/zepto.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())


# Step 2: Make a copy before cleaning
data = df.copy()


# Step 3: Rename columns to simple names
data.columns = [
    "category",
    "name",
    "mrp",
    "discount",
    "available_quantity",
    "selling_price",
    "weight",
    "out_of_stock",
    "quantity",
]


# Step 4: Remove duplicate rows
data = data.drop_duplicates()


# Step 5: Remove products where price is zero
data = data[data["mrp"] > 0]
data = data[data["selling_price"] > 0]


# Step 6: Convert paise to rupees
data["mrp"] = data["mrp"] / 100
data["selling_price"] = data["selling_price"] / 100


# Step 7: Clean out_of_stock column
data["out_of_stock"] = (
    data["out_of_stock"]
    .astype(str)
    .str.lower()
    .map({"true": True, "false": False})
)


# Step 8: Create new business columns
data["revenue"] = data["selling_price"] * data["available_quantity"]
data["inventory_value"] = data["mrp"] * data["available_quantity"]
data["price_per_gram"] = data["selling_price"] / data["weight"].replace(0, pd.NA)
data["estimated_profit"] = (data["selling_price"] * 0.18) * data["available_quantity"]


# Step 9: Create weight buckets
def bucket(x):
    if x < 500:
        return "Small"
    elif x < 1000:
        return "Medium"
    else:
        return "Large"


data["weight_category"] = data["weight"].apply(bucket)


# Step 10: Add synthetic city and warehouse details for dashboard mapping
# These fields are added only for portfolio dashboard practice.
cities = [
    ["Mumbai", "Maharashtra", "West", 19.0760, 72.8777, "WH-MUM-01"],
    ["Delhi", "Delhi", "North", 28.7041, 77.1025, "WH-DEL-01"],
    ["Bengaluru", "Karnataka", "South", 12.9716, 77.5946, "WH-BLR-01"],
    ["Hyderabad", "Telangana", "South", 17.3850, 78.4867, "WH-HYD-01"],
    ["Chennai", "Tamil Nadu", "South", 13.0827, 80.2707, "WH-CHE-01"],
    ["Pune", "Maharashtra", "West", 18.5204, 73.8567, "WH-PUN-01"],
    ["Kolkata", "West Bengal", "East", 22.5726, 88.3639, "WH-KOL-01"],
    ["Ahmedabad", "Gujarat", "West", 23.0225, 72.5714, "WH-AMD-01"],
]

city_data = pd.DataFrame(
    [cities[i % len(cities)] for i in range(len(data))],
    columns=["city", "state", "region", "latitude", "longitude", "warehouse"],
)

data = data.reset_index(drop=True)
data = pd.concat([data, city_data], axis=1)


# Step 11: Add inventory status and revenue band
data["reorder_level"] = 5

data["stock_status"] = "Healthy Stock"
data.loc[data["available_quantity"] <= data["reorder_level"], "stock_status"] = "Low Stock"
data.loc[data["out_of_stock"] == True, "stock_status"] = "Out of Stock"

data["revenue_band"] = "Low Revenue"
data.loc[data["revenue"] >= data["revenue"].quantile(0.50), "revenue_band"] = "Medium Revenue"
data.loc[data["revenue"] >= data["revenue"].quantile(0.80), "revenue_band"] = "High Revenue"


# Step 12: Add sku_id
data.insert(0, "sku_id", range(1, len(data) + 1))


# Step 13: Save cleaned data
data.to_csv("data/processed/zepto_cleaned.csv", index=False)

print("\nCleaned data saved successfully.")
print("Cleaned rows:", len(data))
print("Cleaned file: data/processed/zepto_cleaned.csv")


# Optional: Load data into PostgreSQL
# Run this only when Docker/PostgreSQL is ready:
# python etl.py --load-db
if "--load-db" in sys.argv:
    from sqlalchemy import create_engine

    engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/zepto_analytics")
    data.to_sql("products", engine, if_exists="replace", index=False)
    print("Data loaded into PostgreSQL table: products")
