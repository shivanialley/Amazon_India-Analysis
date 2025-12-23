import pandas as pd
import glob
import os
import re


def load_all_years(
    data_dir=r"C:\Users\Dell\Documents\guvi\Project\Amazon India\data"
):
    """
    Load and merge ALL Amazon India CSV files.

    Supported:
    - amazon_india_YYYY.csv
    - amazon_india_complete_2015_2025.csv
    - amazon_india_products_catalog.csv
    """

    pattern = os.path.join(data_dir, "amazon_india_*.csv")
    files = sorted(glob.glob(pattern))

    if not files:
        raise FileNotFoundError(f"No CSV files found in {data_dir}")

    df_list = []

    for file in files:
        filename = os.path.basename(file)

        # ---- Determine order_year safely ----
        year_match = re.search(r"amazon_india_(\d{4})\.csv", filename)
        range_match = re.search(
            r"amazon_india_complete_(\d{4}_\d{4})\.csv", filename
        )

        if year_match:
            order_year = int(year_match.group(1))
        elif range_match:
            order_year = range_match.group(1)   # '2015_2025'
        else:
            order_year = "catalog"

        df = pd.read_csv(file)
        df["order_year"] = order_year

        df_list.append(df)

        print(f"✅ Loaded {filename} → {df.shape} | order_year={order_year}")

    final_df = pd.concat(df_list, ignore_index=True)

    print("\n📊 FINAL DATASET SUMMARY")
    print("Total Rows :", final_df.shape[0])
    print("Total Cols :", final_df.shape[1])

    return final_df