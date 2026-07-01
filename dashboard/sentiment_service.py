"""
Sentiment Service

This module performs
rule-based sentiment analysis
for user-input economic news.
"""
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.sentiment_utils import (
    assign_sentiment_label,
    convert_sentiment_to_score,
    get_sentiment_keywords
)

# ==========================================
# Clean Text
# ==========================================
import re


def clean_text(text):
    """
    Clean user-input news.

    Parameters
    ----------
    text : str

    Returns
    -------
    text : str
    """

    text = str(text)

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ==========================================
# Analyze News
# ==========================================

def analyze_news(text):
    """
    Analyze user-input news.

    Parameters
    ----------
    text : str

    Returns
    -------
    dict
    """
    cleaned_text = clean_text(text)

    label = assign_sentiment_label(cleaned_text)

    score = convert_sentiment_to_score(
        label
    )

    positive_words, negative_words = (
        get_sentiment_keywords()
    )

    words = cleaned_text.split()

    detected_positive = sorted(
        list(
            {
                word
                for word in words
                if word in positive_words
            }
        )
    )

    detected_negative = sorted(
        list(
            {
                word
                for word in words
                if word in negative_words
            }
        )
    )

    return {

        "text": cleaned_text,

        "label": label,

        "score": score,

        "positive_keywords":
            detected_positive,

        "negative_keywords":
            detected_negative,

    }