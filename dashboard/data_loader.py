"""
Data Loader

Load datasets and trained model
used by the Streamlit dashboard.
"""

import joblib
import pandas as pd
from src.download_assets import download_asset


# from config import (
#     FORECASTING_DATASET,
#     FEATURE_IMPORTANCE_DATASET,
#     NEWS_DATASET,
#     MODEL_PATH
# )


# =====================================================
# Forecasting Dataset
# =====================================================

def load_forecasting_dataset():
    """
    Load forecasting dataset used
    for dashboard statistics.
    """

    try:

        model_path = download_asset(
            "forecasting_dataset.parquet"
        )

        return joblib.load(model_path)

    except Exception as e:

        raise RuntimeError(
            f"Cannot load Forecasting Dataset: {e}"
        )


# =====================================================
# Feature Importance
# =====================================================

def load_feature_importance():
    """
    Load Random Forest
    feature importance.
    """

    try:

        model_path = download_asset(
            "feature_importance.parquet"
        )

        return joblib.load(model_path)

    except Exception as e:

        raise RuntimeError(
            f"Cannot load Feature Importance: {e}"
        )


# =====================================================
# News Dataset
# =====================================================

def load_news_dataset():
    """
    Load news dataset containing
    economic news and sentiment labels.
    """

    try:

        model_path = download_asset(
            "news_with_sentiment.parquet"
        )

        return joblib.load(model_path)

    except Exception as e:

        raise RuntimeError(
            f"Cannot load News with Sentiment: {e}"
        )


# =====================================================
# Random Forest Model
# =====================================================

def load_model():
    """
    Load trained Random Forest model.
    """

    try:

        model_path = download_asset(
            "random_forest.pkl"
        )

        return joblib.load(model_path)

    except Exception as e:

        raise RuntimeError(
            f"Cannot load Random Forest model: {e}"
        )