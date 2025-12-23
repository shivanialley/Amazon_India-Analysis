from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///database/amazon.db")

df = pd.read_csv("data/processed/amazon_cleaned.csv")
df.to_sql("transactions", engine, if_exists="replace", index=False)
