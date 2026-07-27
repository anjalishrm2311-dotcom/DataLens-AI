import pandas as pd


def analyze_missing_values(df: pd.DataFrame):

    missing_df = pd.DataFrame({

        "Column": df.columns,

        "Missing Count": df.isnull().sum().values,

        "Missing Percentage": (
            df.isnull().mean() * 100
        ).round(2).values

    })

    return missing_df.sort_values(
        by="Missing Percentage",
        ascending=False
    )