import pandas as pd


def calculate_quality_score(df: pd.DataFrame):

    total_cells = df.shape[0] * df.shape[1]

    missing_cells = df.isnull().sum().sum()

    duplicate_rows = df.duplicated().sum()

    score = 100

    if total_cells > 0:
        score -= (missing_cells / total_cells) * 50

    if len(df) > 0:
        score -= (duplicate_rows / len(df)) * 50

    return max(0, round(score, 2))