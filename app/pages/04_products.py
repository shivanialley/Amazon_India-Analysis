import streamlit as st
import pandas as pd

df = pd.read_csv("data/processed/amazon_cleaned.csv")

st.title("📦 Product & Inventory Analytics")

# Top Products
top_products = df.groupby("product_name")["final_amount_inr"].sum().sort_values(ascending=False).head(15)
st.bar_chart(top_products)

# Brand Performance
brands = df.groupby("brand")["final_amount_inr"].sum().head(15)
st.bar_chart(brands)

# Ratings vs Sales
st.scatter_chart(
    df[["product_rating", "final_amount_inr"]]
)

st.success("✔ Questions 16–20 Covered")
