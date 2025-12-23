import streamlit as st
import pandas as pd

df = pd.read_csv("data/processed/amazon_cleaned.csv")

st.title("🚚 Operations & Logistics")

# Delivery Performance
delivery = df.groupby("customer_city")["delivery_days"].mean().sort_values().head(15)
st.bar_chart(delivery)

# Payment Methods
payment = df["payment_method"].value_counts()
st.bar_chart(payment)

# Returns
returns = df["return_status"].value_counts()
st.bar_chart(returns)

st.success("✔ Questions 21–25 Covered")
