# IHSG Direction Forecasting Using Economic News Sentiment and Technical Indicators

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![Status](https://img.shields.io/badge/Status-Completed%20v1.0-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

This project develops an end-to-end machine learning pipeline to forecast the next-day direction of the Jakarta Composite Index (IHSG) by combining Indonesian economic news sentiment with technical market indicators. The project includes data preprocessing, feature engineering, model training, and an interactive dashboard built with Streamlit.

## Live Demo

- Streamlit Demo: Coming soon!
- Medium Article: https://medium.com/@chalimasadiah_21544/can-economic-news-predict-the-stock-market-building-an-end-to-end-ml-pipeline-for-ihsg-forecasting-28624649a282?postPublishedType=repub
- GitHub Repository: https://github.com/chalimasadiah/stock-sentiment-prediction
---

## Project Overview

Forecasting stock market movements is challenging because prices are influenced by both historical market behavior and external information such as economic news.

Traditional forecasting models often rely solely on technical indicators, while ignoring textual information that reflects investor sentiment and market expectations.

This project develops an end-to-end machine learning pipeline to forecast the next-day direction of the Jakarta Composite Index (IHSG) by combining Indonesian economic news sentiment with technical market indicators.

The complete workflow includes:

- Collecting Indonesian economic news articles
- Performing rule-based sentiment analysis
- Aggregating daily sentiment scores
- Engineering technical indicators from historical IHSG market data
- Training a Random Forest classifier
- Deploying an interactive Streamlit dashboard for visualization and prediction

The resulting dashboard allows users to explore historical market trends, analyze economic news sentiment, inspect feature importance, and generate next-day IHSG direction predictions.

---

## Project Highlights

✔ End-to-end ML pipeline

✔ Rule-based NLP sentiment analysis

✔ Feature engineering using technical indicators

✔ Random Forest classifier

✔ Interactive Streamlit dashboard

✔ Automatic asset downloading from Hugging Face

✔ Business-oriented insights



---

## Business Problem

Investors and analysts continuously monitor large volumes of financial news before making investment decisions.

However:

- Reading hundreds of news articles every day is inefficient.
- Market reactions are influenced by both sentiment and technical market conditions.
- Combining structured market data with unstructured news data remains a challenge.

This project aims to provide a decision-support tool by integrating both information sources into a machine learning forecasting model.

---

## Dashboard Preview


The Streamlit dashboard provides an interactive interface for exploring market sentiment, historical data, and next-day IHSG direction predictions.

### 1. Dashboard Overview

Displays key project metrics, market summary, and overall dashboard information.

![Overview](assets/image.png)

---

### 2. Economic News Sentiment Analysis

Shows the distribution of positive, neutral, and negative economic news, along with sentiment statistics and recent news analysis.

![Sentiment Analysis](assets/image-1.png)

---

### 3. Business Insight

Provides business-oriented interpretations of market sentiment to help users better understand current market conditions.

![Business Insight](assets/image-2.png)

---

### 4. IHSG Direction Prediction

Allows users to generate next-day IHSG direction predictions using the trained Random Forest model based on technical indicators and aggregated news sentiment.

![Forecasting](assets/image-3.png)

---

### 5. Feature Importance

Visualizes the contribution of each feature used by the Random Forest model, helping explain which variables have the greatest impact on predictions.

![Feature Importance](assets/image-4.png)

---

### 6. Dataset Overview

Summarizes the datasets used throughout the project, including forecasting data, sentiment data, and model inputs.

![Dataset Overview](assets/image-5.png)

---

## Machine Learning Pipeline

```
Raw Economic News
        │
        ▼
Sentiment Analysis (Rule-Based)
        │
        ▼
Daily Sentiment Aggregation
        │
        ▼
Historical IHSG Data (Yahoo Finance)
        │
        ▼
Technical Indicator Engineering (MA, RSI, MACD)
        │
        ▼
Feature Selection
        │
        ▼
Random Forest Classifier
        │
        ▼
Next-Day IHSG Direction Prediction (Up / Down)
        │
        ▼
Interactive Dashboard & Business Insight
```

---

## Dataset

To keep this repository lightweight, datasets and trained models are not tracked in Git.

The dashboard automatically loads required assets in the following order:

1. Local sample_data/
2. Local models/
3. Hugging Face Dataset Repository

Dataset repository:

[stock-sentiment-assets](https://huggingface.co/datasets/chalimasadiah/stock-sentiment-assets)

**Data Sources:**

| Source                                                                                  | Content                                                            |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| [Huggingface.co](https://huggingface.co/datasets/fahadh4ilyas/indonesian_news_datasets) | ~6,800 Indonesian economic news articles                           |
| [Yahoo Finance](https://finance.yahoo.com)                                              | Historical IHSG daily market data (Open, High, Low, Close, Volume) |

---

## Features

- Economic News Sentiment Analysis
- IHSG Direction Prediction (Up / Down)
- Technical Indicator Visualization
- Feature Importance Analysis
- Historical Market Trend Visualization
- Interactive Dashboard
- Dataset Overview
- Business Insight Summary

---

## Model Performance

| Model                          | Accuracy  |
| ------------------------------ | --------- |
| Logistic Regression (Baseline) | 37.5%     |
| **Random Forest**              | **75.0%** |

> The Random Forest classifier correctly predicted the next-day IHSG direction approximately **3 out of every 4 times** on the validation set.

---

## Tech Stack

| Category         | Tools                       |
| ---------------- | --------------------------- |
| Language         | Python 3.12                 |
| Machine Learning | Scikit-learn, Pandas, NumPy |
| Visualization    | Plotly, Matplotlib          |
| Dashboard        | Streamlit                   |
| Version Control  | Git, GitHub                 |

---

## Installation

**1. Clone the repository**

```bash
git clone git@github.com:chalimasadiah/stock-sentiment-prediction.git
cd stock_sentiment_prediction
```

**2. Create a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate        # Mac / Linux
.venv\Scripts\activate           # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the dashboard**

```bash
streamlit run dashboard/app.py
```
If local assets are unavailable, the dashboard automatically downloads them from the Hugging Face Dataset repository.

No additional manual download is required.
---

## Project Structure

```
stock_sentiment_prediction/

├── Dockerfile
├── README.md
├── assets
│   ├── image-1.png
│   ├── image-2.png
│   ├── image-3.png
│   ├── image-4.png
│   ├── image-5.png
│   └── image.png
├── dashboard
│   ├── app.py
│   ├── assets
│   ├── components
│   ├── config.py
│   ├── data_loader.py
│   └── sentiment_service.py
├── sample_data                 # downloaded automatically
├── models                      # downloaded automatically
├── notebooks
│   ├── 01_news_dataset_eda.ipynb
│   ├── 02_sentiment_analysis.ipynb
│   ├── 02a_manual_labeling.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_modeling.ipynb
├── requirements.txt
├── scripts
│   └── prepare_sample_data.py
└── src
    ├── __init__.py
    ├── data_io.py
    ├── data_validation.py
    ├── download_assets.py
    └── sentiment_utils.py
```
Models and sample datasets are downloaded automatically from the Hugging Face Dataset repository when unavailable locally.
---

## Model Performance

| Metric | Value |
|---------|-------|
| Accuracy | 75% |
| Validation Strategy | Chronological Train-Test Split |

## Current Status

## Current Status

| Item | Status |
|------|--------|
| Current Version | v1.0 |
| Project Status | Baseline Implementation Completed |
| Deployment | GitHub + Hugging Face Spaces |
| Next Milestone | Real-time Prediction |

---

## Next milestone

Real-time prediction

---

## Future Development
Version 2

- Historical Backtesting
- Live Prediction

Version 3

- IndoBERT Sentiment

Version 4

- FastAPI Backend
- Next.js Frontend

Version 5

- Docker
- Cloud Deployment



## References

- [Yahoo Finance](https://finance.yahoo.com)
- [Huggingface.co](https://huggingface.co/datasets/fahadh4ilyas/indonesian_news_datasets)
- [Scikit-learn Documentation](https://scikit-learn.org)
- [Streamlit Documentation](https://streamlit.io)
- [Plotly Documentation](https://plotly.com)
- Breiman, L. (2001). Random Forests. _Machine Learning_, 45(1), 5–32.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgement

Built as the final project for the **Pacmann Machine Learning Program**.

---

## Author

**Chalima Sadiah**

Interested in Machine Learning Engineering, Applied AI, Forecasting, and Decision Support Systems.

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/chalimasadiah)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/chalimasadiah/)
[![Medium](https://img.shields.io/badge/Medium-Article-black?logo=medium)](https://medium.com/@chalimasadiah_21544)

> Feel free to connect or provide feedback about this project.
