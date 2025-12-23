import mlflow
import mlflow.sklearn
from src.config import logger
from sklearn.metrics import r2_score, mean_absolute_error

mlflow.set_experiment("Amazon-Sales-Forecast")

with mlflow.start_run(run_name="RandomForest_v1"):

    logger.info("Training started")

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    r2 = r2_score(y_test, preds)
    mae = mean_absolute_error(y_test, preds)

    # Metrics
    mlflow.log_metric("r2_score", r2)
    mlflow.log_metric("mae", mae)

    # Params
    mlflow.log_param("model", "RandomForest")
    mlflow.log_param("n_estimators", 200)

    # Model artifact
    mlflow.sklearn.log_model(model, "model")

    logger.info("Training completed")