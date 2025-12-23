from src.data_loader import load_all_years
from src.cleaning import clean_data

print("🔄 Loading yearly CSV files...")
df = load_all_years("data")

print("🧹 Cleaning data...")
df_clean = clean_data(df)

df_clean.to_csv("data/processed/amazon_cleaned.csv", index=False)

print("✅ All 13 CSV files merged & cleaned successfully")
