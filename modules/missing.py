import pandas as pd


def analyze_missing_values(df: pd.DataFrame):

    missing_count = df.isna().sum()

    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Count": missing_count.values,
        "Missing Percentage": (
            missing_count / len(df) * 100
        ).round(2).values
    })

    return missing_df.sort_values(
        by="Missing Percentage",
        ascending=False
    )