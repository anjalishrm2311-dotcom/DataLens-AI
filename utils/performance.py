import pandas as pd


def is_large_dataset(df: pd.DataFrame):

    return len(df) >= 100000


def sample_dataframe(
    df: pd.DataFrame,
    sample_size=50000
):

    if len(df) > sample_size:

        return df.sample(
            sample_size,
            random_state=42
        )

    return df