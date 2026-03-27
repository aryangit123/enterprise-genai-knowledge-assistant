import mlflow
import os
from config import MLFLOW_EXPERIMENT_NAME, MLFLOW_TRACKING_URI, EMBEDDING_MODEL, LLM_MODEL, RETRIEVAL_K
from logger import get_logger

logger = get_logger(__name__)

def setup_mlflow():
    """Setup MLflow tracking."""
    try:
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        logger.info(f"MLflow tracking URI set to: {MLFLOW_TRACKING_URI}")
    except Exception as e:
        logger.warning(f"Could not set MLflow tracking URI: {str(e)}")

def start_experiment():
    """Start MLflow experiment."""
    try:
        setup_mlflow()
        mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)
        logger.info(f"MLflow experiment set to: {MLFLOW_EXPERIMENT_NAME}")
    except Exception as e:
        logger.warning(f"Could not set MLflow experiment: {str(e)}")

def track_model_params():
    """Track model parameters in MLflow."""
    try:
        with mlflow.start_run():
            mlflow.log_param("embedding_model", EMBEDDING_MODEL)
            mlflow.log_param("llm_model", LLM_MODEL)
            mlflow.log_param("vector_db", "FAISS")
            mlflow.log_param("retrieval_k", RETRIEVAL_K)
            
            logger.info("Model parameters logged to MLflow")
    except Exception as e:
        logger.warning(f"Could not log parameters to MLflow: {str(e)}")

def track_metrics(metrics_dict):
    """Track metrics in MLflow."""
    try:
        with mlflow.start_run():
            for key, value in metrics_dict.items():
                if isinstance(value, (int, float)):
                    mlflow.log_metric(key, value)
            
            logger.info(f"Logged {len(metrics_dict)} metrics to MLflow")
    except Exception as e:
        logger.warning(f"Could not log metrics to MLflow: {str(e)}")

def track_artifact(file_path):
    """Track artifact in MLflow."""
    try:
        with mlflow.start_run():
            mlflow.log_artifact(file_path)
            logger.info(f"Logged artifact to MLflow: {file_path}")
    except Exception as e:
        logger.warning(f"Could not log artifact to MLflow: {str(e)}")

# Convenience function for experiment tracking
def track_experiment():
    """Track experiment with default parameters."""
    start_experiment()
    track_model_params()