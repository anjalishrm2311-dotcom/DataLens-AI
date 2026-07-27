import pandas as pd


def is_large_dataset(df: pd.DataFrame):
    return len(df) >= 100000


def sample_dataframe(
    df: pd.DataFrame,
    sample_size=10000
):
    """
    Return a representative sample for charts and profiling.
    Keeps the app responsive for large datasets.
    """

    if len(df) <= sample_size:
        return df

    return df.sample(
        n=sample_size,
        random_state=42
    )