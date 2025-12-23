import pandas as pd
from sklearn.metrics import mean_absolute_error
from src.config import logger

def monitor_model(model, df):
    X = df[["year","month","discount_percent"]]
    y = df["final_amount_inr"]

    preds = model.predict(X)
    mae = mean_absolute_error(y, preds)

    logger.info(f"Monitoring MAE: {mae}")
    return mae
