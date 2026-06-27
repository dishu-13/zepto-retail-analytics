import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Zepto Retail Analytics", layout="wide")


# Load cleaned data
data = pd.read_csv("data/processed/zepto_cleaned.csv")


st.title("Zepto Retail Intelligence Dashboard")
st.caption("City, region, warehouse, and location columns are synthetic fields added for portfolio dashboard practice.")


# Sidebar filters
st.sidebar.header("Filters")

category_filter = st.sidebar.multiselect(
    "Select Category",
    sorted(data["category"].unique()),
    default=sorted(data["category"].unique()),
)

region_filter = st.sidebar.multiselect(
    "Select Region",
    sorted(data["region"].unique()),
    default=sorted(data["region"].unique()),
)

city_filter = st.sidebar.multiselect(
    "Select City",
    sorted(data["city"].unique()),
    default=sorted(data["city"].unique()),
)

stock_filter = st.sidebar.multiselect(
    "Select Stock Status",
    sorted(data["stock_status"].unique()),
    default=sorted(data["stock_status"].unique()),
)

discount_range = st.sidebar.slider(
    "Discount Range",
    int(data["discount"].min()),
    int(data["discount"].max()),
    (int(data["discount"].min()), int(data["discount"].max())),
)

page = st.sidebar.radio(
    "Dashboard Page",
    ["Executive", "Revenue", "Inventory", "Location", "Product Search"],
)


# Apply filters
filtered_data = data[
    (data["category"].isin(category_filter))
    & (data["region"].isin(region_filter))
    & (data["city"].isin(city_filter))
    & (data["stock_status"].isin(stock_filter))
    & (data["discount"] >= discount_range[0])
    & (data["discount"] <= discount_range[1])
]


if filtered_data.empty:
    st.warning("No data found for selected filters.")
    st.stop()


# KPI values
total_revenue = filtered_data["revenue"].sum()
inventory_value = filtered_data["inventory_value"].sum()
estimated_profit = filtered_data["estimated_profit"].sum()
total_products = filtered_data["sku_id"].count()
out_of_stock = filtered_data[filtered_data["out_of_stock"] == True]["sku_id"].count()
average_discount = filtered_data["discount"].mean()


# KPI cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"Rs {total_revenue:,.0f}")
col2.metric("Inventory Value", f"Rs {inventory_value:,.0f}")
col3.metric("Estimated Profit", f"Rs {estimated_profit:,.0f}")

col4, col5, col6 = st.columns(3)
col4.metric("Total Products", f"{total_products:,}")
col5.metric("Out of Stock", f"{out_of_stock:,}")
col6.metric("Average Discount", f"{average_discount:.1f}%")


if page == "Executive":
    st.subheader("Executive Overview")

    revenue_category = filtered_data.groupby("category")["revenue"].sum().reset_index()
    revenue_category = revenue_category.sort_values(by="revenue", ascending=False)

    stock_status = filtered_data.groupby("stock_status")["sku_id"].count().reset_index()
    stock_status.columns = ["stock_status", "products"]

    city_revenue = filtered_data.groupby("city")["revenue"].sum().reset_index()
    city_revenue = city_revenue.sort_values(by="revenue", ascending=False)

    c1, c2 = st.columns(2)

    fig1 = px.bar(
        revenue_category,
        x="category",
        y="revenue",
        color="category",
        title="Revenue by Category",
    )
    c1.plotly_chart(fig1, width="stretch")

    fig2 = px.pie(
        stock_status,
        names="stock_status",
        values="products",
        title="Stock Status Split",
        hole=0.45,
    )
    c2.plotly_chart(fig2, width="stretch")

    c3, c4 = st.columns(2)

    fig3 = px.treemap(
        filtered_data,
        path=["region", "city", "category"],
        values="revenue",
        title="Revenue Treemap by Region, City, and Category",
    )
    c3.plotly_chart(fig3, width="stretch")

    fig4 = px.bar(
        city_revenue,
        x="city",
        y="revenue",
        color="city",
        title="Revenue by City",
    )
    c4.plotly_chart(fig4, width="stretch")

    top_category = revenue_category.iloc[0]["category"]
    top_city = city_revenue.iloc[0]["city"]

    st.info(f"Top category is {top_category}. Top city by revenue is {top_city}.")


elif page == "Revenue":
    st.subheader("Revenue Analysis")

    top_products = filtered_data.sort_values(by="revenue", ascending=False).head(15)
    discount_revenue = filtered_data.groupby("discount")["revenue"].sum().reset_index()
    revenue_band = filtered_data.groupby("revenue_band")["sku_id"].count().reset_index()
    revenue_band.columns = ["revenue_band", "products"]

    c1, c2 = st.columns(2)

    fig1 = px.bar(
        top_products,
        x="revenue",
        y="name",
        color="category",
        orientation="h",
        title="Top 15 Products by Revenue",
    )
    c1.plotly_chart(fig1, width="stretch")

    fig2 = px.line(
        discount_revenue,
        x="discount",
        y="revenue",
        markers=True,
        title="Revenue by Discount Percentage",
    )
    c2.plotly_chart(fig2, width="stretch")

    c3, c4 = st.columns(2)

    fig3 = px.scatter(
        filtered_data,
        x="discount",
        y="revenue",
        size="available_quantity",
        color="category",
        hover_name="name",
        title="Discount vs Revenue",
    )
    c3.plotly_chart(fig3, width="stretch")

    fig4 = px.pie(
        revenue_band,
        names="revenue_band",
        values="products",
        title="Product Count by Revenue Band",
    )
    c4.plotly_chart(fig4, width="stretch")

    st.dataframe(
        top_products[
            [
                "name",
                "category",
                "city",
                "selling_price",
                "discount",
                "available_quantity",
                "revenue",
                "estimated_profit",
            ]
        ],
        width="stretch",
    )


elif page == "Inventory":
    st.subheader("Inventory Analysis")

    inventory_category = filtered_data.groupby("category")["inventory_value"].sum().reset_index()
    inventory_category = inventory_category.sort_values(by="inventory_value", ascending=False)

    stock_risk = filtered_data.groupby(["category", "stock_status"])["sku_id"].count().reset_index()
    stock_risk.columns = ["category", "stock_status", "products"]

    reorder_data = filtered_data[filtered_data["stock_status"].isin(["Low Stock", "Out of Stock"])]
    reorder_data = reorder_data.sort_values(by=["stock_status", "revenue"], ascending=[True, False])

    c1, c2 = st.columns(2)

    fig1 = px.bar(
        inventory_category,
        x="category",
        y="inventory_value",
        color="category",
        title="Inventory Value by Category",
    )
    c1.plotly_chart(fig1, width="stretch")

    fig2 = px.bar(
        stock_risk,
        x="category",
        y="products",
        color="stock_status",
        title="Stock Status by Category",
    )
    c2.plotly_chart(fig2, width="stretch")

    fig3 = px.box(
        filtered_data,
        x="category",
        y="available_quantity",
        color="category",
        title="Available Quantity Distribution",
    )
    st.plotly_chart(fig3, width="stretch")

    st.subheader("Reorder Suggestions")
    st.dataframe(
        reorder_data[
            [
                "name",
                "category",
                "city",
                "warehouse",
                "available_quantity",
                "reorder_level",
                "stock_status",
                "revenue",
            ]
        ].head(50),
        width="stretch",
    )


elif page == "Location":
    st.subheader("Location Analysis")

    city_summary = (
        filtered_data.groupby(["city", "state", "region", "latitude", "longitude"])
        .agg(
            revenue=("revenue", "sum"),
            inventory_value=("inventory_value", "sum"),
            products=("sku_id", "count"),
            out_of_stock=("out_of_stock", "sum"),
        )
        .reset_index()
    )

    fig1 = px.scatter_map(
        city_summary,
        lat="latitude",
        lon="longitude",
        size="revenue",
        color="region",
        hover_name="city",
        hover_data=["state", "products", "out_of_stock", "inventory_value"],
        title="Revenue Map by City",
        zoom=4,
        height=520,
    )
    st.plotly_chart(fig1, width="stretch")

    c1, c2 = st.columns(2)

    fig2 = px.bar(
        city_summary.sort_values(by="revenue", ascending=False),
        x="city",
        y="revenue",
        color="region",
        title="City Revenue Ranking",
    )
    c1.plotly_chart(fig2, width="stretch")

    fig3 = px.bar(
        city_summary.sort_values(by="out_of_stock", ascending=False),
        x="city",
        y="out_of_stock",
        color="region",
        title="Out of Stock Products by City",
    )
    c2.plotly_chart(fig3, width="stretch")

    st.dataframe(city_summary, width="stretch")


else:
    st.subheader("Product Search")

    search = st.text_input("Search product name")

    if search:
        result = filtered_data[filtered_data["name"].str.contains(search, case=False, na=False)]
    else:
        result = filtered_data.head(50)

    st.dataframe(
        result[
            [
                "sku_id",
                "name",
                "category",
                "city",
                "warehouse",
                "mrp",
                "selling_price",
                "discount",
                "available_quantity",
                "stock_status",
                "revenue",
                "price_per_gram",
            ]
        ],
        width="stretch",
    )


st.download_button(
    "Download Filtered Report",
    filtered_data.to_csv(index=False),
    "zepto_filtered_report.csv",
    "text/csv",
)
