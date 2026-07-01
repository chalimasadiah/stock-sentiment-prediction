def get_sentiment_keywords():
    """
    Return positive and negative
    economic sentiment keywords.
    """
    positive_words = [
    "laba",
    "untung",
    "naik",
    "menaikkan",
    "kenaikan",
    "menguat",
    "penguatan",
    "ekspansi",
    "investasi",
    "tumbuh",
    "pertumbuhan",
    "buyback"
    ]

    negative_words = [
    "bangkrut",
    "rugi",
    "turun",
    "menurun",
    "penurunan",
    "melemah",
    "pelemahan",
    "resesi",
    "krisis"
    ]
    return positive_words, negative_words



def assign_sentiment_label(text):
    """
    Assign sentiment label to a news text.

    Parameters
    ----------
    text : str
        Input news text.

    Returns
    -------
    str
        Sentiment label.
    """
    positive_words, negative_words = get_sentiment_keywords()

    words = str(text).lower().split()

    # Positive word count
    pos_count = sum(1 for word in words if word in positive_words)
    
    # Negative word count
    neg_count = sum(1 for word in words if word in negative_words)

    # Comparing and Labeling
    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"


def convert_sentiment_to_score(label):
    """
    Convert sentiment label into numerical score.
    """

    mapping = {
        "Positive": 1,
        "Neutral": 0,
        "Negative": -1
    }

    if label not in mapping:
        raise ValueError(
            f"Invalid sentiment label: {label}"
        )

    return mapping[label]
