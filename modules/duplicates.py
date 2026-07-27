import pandas as pd


def analyze_duplicates(df: pd.DataFrame):

    duplicate_rows = df[df.duplicated()]

    return duplicate_rows