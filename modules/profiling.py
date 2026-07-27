import pandas as pd
from pandas.api.types import (
    is_numeric_dtype,
    is_string_dtype
)


# =====================================================
# Numeric Column Profiling
# =====================================================

def profile_numeric_columns(df: pd.DataFrame):

    numeric_cols = df.select_dtypes(include="number").columns

    profiling_data = []

    for col in numeric_cols:

        profiling_data.append({

            "Column": col,

            "Mean": round(df[col].mean(), 2),

            "Median": round(df[col].median(), 2),

            "Min": df[col].min(),

            "Max": df[col].max(),

            "Std Dev": round(df[col].std(), 2),

            "Variance": round(df[col].var(), 2),

            "Missing Values": int(df[col].isnull().sum()),

            "Missing %": round(df[col].isnull().mean() * 100, 2),

            "Unique Values": int(df[col].nunique())

        })

    return pd.DataFrame(profiling_data)


# =====================================================
# Categorical Column Profiling
# =====================================================

def profile_categorical_columns(df: pd.DataFrame):

    categorical_cols = df.select_dtypes(
        include=["object", "string", "category"]
    ).columns

    profiling_data = []

    for col in categorical_cols:

        mode = df[col].mode()

        profiling_data.append({

            "Column": col,

            "Most Frequent": mode.iloc[0] if not mode.empty else "N/A",

            "Unique Values": int(df[col].nunique()),

            "Missing Values": int(df[col].isnull().sum()),

            "Missing %": round(df[col].isnull().mean() * 100, 2)

        })

    return pd.DataFrame(profiling_data)


# =====================================================
# Dataset Profiling Summary
# =====================================================

def dataset_profile(df: pd.DataFrame):

    profile = {

        "Rows": df.shape[0],

        "Columns": df.shape[1],

        "Memory Usage (MB)": round(
            df.memory_usage(deep=True).sum() / (1024 * 1024),
            2
        ),

        "Numeric Columns":
            len(df.select_dtypes(include="number").columns),

        "Categorical Columns":
            len(df.select_dtypes(include=["object", "string"]).columns),

        "Datetime Columns":
            len(df.select_dtypes(include="datetime").columns),

        "Duplicate Rows":
            int(df.duplicated().sum()),

        "Missing Values":
            int(df.isnull().sum().sum())
    }

    return profile