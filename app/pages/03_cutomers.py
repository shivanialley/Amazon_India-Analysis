import streamlit as st
import pandas as pd

df = pd.read_csv("data/processed/amazon_cleaned.csv")

st.title("👥 Customer Analytics")

# RFM-like metrics
rfm = df.groupby("customer_id").agg(
    frequency=("transaction_id", "count"),
    monetary=("final_amount_inr", "sum")
)

st.bar_chart(rfm["monetary"].sort_values(ascending=False).head(20))

# Prime vs Non-Prime
prime = df.groupby("is_prime_member")["final_amount_inr"].mean()
st.bar_chart(prime)

# Age behavior
age = df.groupby("age_group")["final_amount_inr"].mean()
st.bar_chart(age)

st.success("✔ Questions 11–15 Covered")