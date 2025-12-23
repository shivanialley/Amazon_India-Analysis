import streamlit as st
import pandas as pd
import joblib

df = pd.read_csv("data/processed/amazon_cleaned.csv")

st.title("🧠 Advanced Analytics")

# Sales Forecast
model = joblib.load("models/sales_forecast.pkl")

year = st.number_input("Year", 2026, 2030, 2027)
month = st.slider("Month", 1, 12, 6)
discount = st.slider("Discount %", 0, 80, 10)

pred = model.predict([[year, month, discount]])[0]
st.metric("Forecasted Revenue", f"₹{pred:,.0f}")

st.success("✔ Questions 26–30 Covered")