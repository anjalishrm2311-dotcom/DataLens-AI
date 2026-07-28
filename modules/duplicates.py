import pandas as pd


def analyze_duplicates(df: pd.DataFrame):

    duplicate_count = int(df.duplicated().sum())

    if duplicate_count == 0:
        return pd.DataFrame()

    # Return only a preview of duplicates
    duplicate_rows = df[df.duplicated()].head(100)

    return duplicate_rows