import pandas as pd


def get_dataset_summary(df: pd.DataFrame):

    summary = {}

    summary["Rows"] = df.shape[0]

    summary["Columns"] = df.shape[1]

    summary["Memory Usage"] = round(
        df.memory_usage(deep=True).sum() / (1024 * 1024),
        2
    )

    summary["Numeric Columns"] = len(
        df.select_dtypes(include="number").columns
    )

    summary["Categorical Columns"] = len(
        df.select_dtypes(include="object").columns
    )

    summary["Datetime Columns"] = len(
        df.select_dtypes(include="datetime").columns
    )

    summary["Missing Values"] = int(df.isnull().sum().sum())

    summary["Duplicate Rows"] = int(df.duplicated().sum())

    return summary