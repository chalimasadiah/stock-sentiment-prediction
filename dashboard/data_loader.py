"""
Data Loader

Load datasets and trained model
used by the Streamlit dashboard.
"""

import joblib
import pandas as pd

from config import (
    FORECASTING_DATASET,
    FEATURE_IMPORTANCE_DATASET,
    NEWS_DATASET,
    MODEL_PATH
)


# =====================================================
# Forecasting Dataset
# =====================================================

def load_forecasting_dataset():
    """
    Load forecasting dataset used
    for dashboard statistics.
    """

    return pd.read_parquet(
        FORECASTING_DATASET
    )


# =====================================================
# Feature Importance
# =====================================================

def load_feature_importance():
    """
    Load Random Forest
    feature importance.
    """

    return pd.read_parquet(
        FEATURE_IMPORTANCE_DATASET
    )


# =====================================================
# News Dataset
# =====================================================

def load_news_dataset():
    """
    Load news dataset containing
    economic news and sentiment labels.
    """

    return pd.read_parquet(
        NEWS_DATASET
    )


# =====================================================
# Random Forest Model
# =====================================================

def load_model():
    """
    Load trained Random Forest model.
    """

    return joblib.load(
        MODEL_PATH
    )