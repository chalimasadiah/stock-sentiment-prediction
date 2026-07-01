import pandas as pd

def load_dataframe(file_path):
    """
    Load a dataframe from a file path.

    Parameters
    ----------
    file_path : str
        Path to the dataset file.
    
    Returns
    -------
    pandas.DataFrame
        Loaded dataframe.
    """

    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    
    elif file_path.endswith(".parquet"):
        return pd.read_parquet(file_path)

    elif file_path.endswith(".pkl"):
        return pd.read_pickle(file_path)
    
    else:
        raise ValueError(
            "Unsupported file format."
        )



def save_dataframe(df, file_path):
    """
    Save dataframe to disk.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe to save.
    
    file_path : str
        Output file path.
    """

    if file_path.endswith(".csv"):
        df.to_csv(
            file_path,
            index=False
        )
    
    elif file_path.endswith(".parquet"):
        df.to_parquet(
            file_path,
            index=False
        )
    
    elif file_path.endswith(".pkl"):
        df.to_pickle(
            file_path
        )
    
    else:
        raise ValueError(
            "Unsupported file format."
        )
    