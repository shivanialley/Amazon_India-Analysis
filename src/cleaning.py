import pandas as pd
import numpy as np

def clean_data(df):

    # Date handling
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Prices
    df["original_price_inr"] = (
        df["original_price_inr"]
        .astype(str)
        .str.replace("₹", "")
        .str.replace(",", "")
    )
    df["original_price_inr"] = pd.to_numeric(df["original_price_inr"], errors="coerce")

    df["final_amount_inr"] = pd.to_numeric(
        df["final_amount_inr"], errors="coerce"
    )

    # Boolean standardization
    bool_map = {"Yes": True, "No": False, "Y": True, "N": False, 1: True, 0: False}
    for col in ["is_prime_member", "is_festival_sale"]:
        if col in df.columns:
            df[col] = df[col].map(bool_map)

    # City normalization
    city_map = {
        "Bangalore": "Bengaluru",
        "Bombay": "Mumbai",
        "New Delhi": "Delhi"
    }
    df["customer_city"] = df["customer_city"].replace(city_map)

    # Remove invalid rows
    df = df.dropna(subset=["order_date", "final_amount_inr"])

    # Remove duplicates
    df = df.drop_duplicates()

    return df