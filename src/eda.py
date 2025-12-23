import matplotlib.pyplot as plt
import seaborn as sns

def revenue_trend(df):
    yearly = df.groupby(df["order_date"].dt.year)["final_amount_inr"].sum()
    yearly.plot(kind="line", marker="o")
    plt.title("Yearly Revenue Trend")
    plt.xlabel("Year")
    plt.ylabel("Revenue (INR)")
    plt.show()