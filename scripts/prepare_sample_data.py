import pandas as pd

news = pd.read_parquet(
    "data/interim/news_with_sentiment.parquet"
)

sample_news = news.tail(200)

sample_news.to_parquet(
    "sample_data/news_with_sentiment.parquet",
    index=False
)

print("Done")