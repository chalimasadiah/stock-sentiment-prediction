"""
Data Loader

Load datasets and trained model
used by the Streamlit dashboard.
"""

import joblib
import pandas as pd

from src.download_assets import download_asset


# =====================================================
# Forecasting Dataset
# =====================================================

def load_forecasting_dataset():
    """
    Load forecasting dataset.
    """

    try:
        path = download_asset(
            "forecasting_dataset.csv"
        )

        return pd.read_csv(path)

    except Exception as e:
        raise RuntimeError(
            f"Cannot load Forecasting Dataset: {e}"
        )


# =====================================================
# Feature Importance
# =====================================================

def load_feature_importance():
    """
    Load feature importance.
    """

    try:
        path = download_asset(
            "feature_importance.csv"
        )

        return pd.read_csv(path)

    except Exception as e:
        raise RuntimeError(
            f"Cannot load Feature Importance: {e}"
        )


# =====================================================
# News Dataset
# =====================================================

def load_news_dataset():
    """
    Load news dataset.
    """

    try:
        path = download_asset(
            "news_with_sentiment.csv"
        )

        return pd.read_csv(path)

    except Exception as e:
        raise RuntimeError(
            f"Cannot load News Dataset: {e}"
        )


# =====================================================
# Random Forest Model
# =====================================================

def load_model():
    """
    Load trained Random Forest model.
    """

    try:
        path = download_asset(
            "random_forest.pkl"
        )

        return joblib.load(path)

    except Exception as e:
        raise RuntimeError(
            f"Cannot load Random Forest Model: {e}"
        )