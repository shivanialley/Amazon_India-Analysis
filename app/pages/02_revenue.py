import streamlit as st
import pandas as pd

df = pd.read_csv("data/processed/amazon_cleaned.csv")
df["month"] = pd.to_datetime(df["order_date"]).dt.month

st.title("💰 Revenue Analytics")

# Revenue Trend
trend = df.groupby(["order_year", "month"])["final_amount_inr"].sum().unstack()
st.line_chart(trend.T)

# Category Performance
category_rev = df.groupby("category")["final_amount_inr"].sum()
st.bar_chart(category_rev)

# Festival Impact
festival = df.groupby("is_festival_sale")["final_amount_inr"].sum()
st.bar_chart(festival)

# Discount vs Revenue
st.scatter_chart(
    df[["discount_percent", "final_amount_inr"]]
)

st.success("✔ Questions 6–10 Covered")