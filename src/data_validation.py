import pandas as pd

def check_missing_values(df):
    """
    Calculate missing values for each column.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    Returns
    -------
    pandas.Series
        Missing value count per column.
    """

    return df.isnull().sum()


def check_duplicate_titles(df):
    """
    Count duplicated news titles.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    Returns
    -------
    int
        Number of duplicated titles.
    """

    return df["title"].duplicated().sum()



def calculate_text_length(df, column):
    """
    Calculate text length in words.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    column : str
        Text column.

    Returns
    -------
    pandas.Series
        Word count.
    """
    return (
        df[column].fillna("").apply(
            lambda x: len(str(x).split())
        )
    )
