def create_features(df):
    df["year"] = df["order_date"].dt.year
    df["month"] = df["order_date"].dt.month

    df["discount_amount"] = (
        df["original_price_inr"] * df["discount_percent"] / 100
    )

    return df