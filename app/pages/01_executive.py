import streamlit as st
import pandas as pd

df = pd.read_csv("data/processed/amazon_cleaned.csv")

st.title("📊 Executive Dashboard")

# KPIs
total_revenue = df["final_amount_inr"].sum()
active_customers = df["customer_id"].nunique()
avg_order_value = df["final_amount_inr"].mean()
top_category = df.groupby("category")["final_amount_inr"].sum().idxmax()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Active Customers", active_customers)
col3.metric("Avg Order Value", f"₹{avg_order_value:,.0f}")
col4.metric("Top Category", top_category)

# YoY Growth
yoy = df.groupby("order_year")["final_amount_inr"].sum().pct_change() * 100
st.line_chart(yoy)

st.success("✔ Questions 1–5 Covered")
