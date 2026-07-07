"""
Dashboard Configuration

Global configuration used across
the Streamlit dashboard.
"""

from pathlib import Path

# ==================================================
# Project Root
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==================================================
# Folder Paths
# ==================================================

SAMPLE_FOLDER = BASE_DIR / "sample_data"

MODEL_FOLDER = BASE_DIR / "models"

ASSETS_FOLDER = Path(__file__).resolve().parent / "assets"

# ==================================================
# Dataset Paths
# ==================================================

FORECASTING_DATASET = (
    SAMPLE_FOLDER /
    "forecasting_dataset.csv"
)

FEATURE_IMPORTANCE_DATASET = (
    SAMPLE_FOLDER /
    "feature_importance.csv"
)

NEWS_DATASET = (
    SAMPLE_FOLDER /
    "news_with_sentiment.csv"
)

MODEL_PATH = (
    MODEL_FOLDER /
    "random_forest.pkl"
)

# ==================================================
# Dashboard Information
# ==================================================

APP_TITLE = "Stock Market Movement Prediction"

APP_SUBTITLE = (
    "Predicting IHSG Direction "
    "Using Economic News Sentiment"
)

PROJECT_DESCRIPTION = (
    "This dashboard predicts the "
    "next-day IHSG movement based "
    "on economic news sentiment."
)

# ==================================================
# Model Information
# ==================================================

MODEL_NAME = "Random Forest"

MODEL_ACCURACY = 0.75

MODEL_PRECISION = 0.80

MODEL_RECALL = 0.67

MODEL_F1 = 0.73

# ==================================================
# Dataset Information
# ==================================================

DATASET_SIZE = "6,867 News Articles"

DATA_PERIOD = (
    "March 2023 – April 2023"
)

TARGET = (
    "Next-Day IHSG Direction"
)

# ==================================================
# Theme
# ==================================================

PRIMARY_COLOR = "#2563eb"

POSITIVE_COLOR = "#16a34a"

NEGATIVE_COLOR = "#dc2626"

NEUTRAL_COLOR = "#f59e0b"

BACKGROUND_COLOR = "#f8fafc"


# ==================================================
# Hugging Face Dataset Repository
# ==================================================

HF_DATASET_REPO = "chalimasadiah/stock-sentiment-assets"