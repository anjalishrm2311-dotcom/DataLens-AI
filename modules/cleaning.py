import pandas as pd
from pandas.api.types import (
    is_numeric_dtype,
    is_string_dtype,
    is_datetime64_any_dtype
)


# =====================================================
# Remove Duplicate Rows
# =====================================================

def remove_duplicates(df: pd.DataFrame):
    """
    Remove duplicate rows from the dataset.
    """

    cleaned_df = df.drop_duplicates()

    removed = len(df) - len(cleaned_df)

    return cleaned_df, removed


# =====================================================
# Remove Completely Empty Rows
# =====================================================

def remove_empty_rows(df: pd.DataFrame):
    """
    Remove rows where all values are missing.
    """

    cleaned_df = df.dropna(how="all")

    removed = len(df) - len(cleaned_df)

    return cleaned_df, removed


# =====================================================
# Fill Missing Values
# =====================================================

def fill_missing_values(df: pd.DataFrame):
    """
    Fill missing values according to data type.

    Numeric Columns   -> Median
    String Columns    -> Mode
    Datetime Columns  -> Mode
    """

    cleaned_df = df.copy()

    for column in cleaned_df.columns:

        # ----------------------------
        # Numeric Columns
        # ----------------------------
        if is_numeric_dtype(cleaned_df[column]):

            median = cleaned_df[column].median()

            cleaned_df[column] = cleaned_df[column].fillna(median)

        # ----------------------------
        # Datetime Columns
        # ----------------------------
        elif is_datetime64_any_dtype(cleaned_df[column]):

            mode = cleaned_df[column].mode()

            if not mode.empty:
                cleaned_df[column] = cleaned_df[column].fillna(mode.iloc[0])

        # ----------------------------
        # String / Object Columns
        # ----------------------------
        elif (
            is_string_dtype(cleaned_df[column])
            or cleaned_df[column].dtype == "object"
        ):

            mode = cleaned_df[column].mode()

            if not mode.empty:
                cleaned_df[column] = cleaned_df[column].fillna(mode.iloc[0])

    return cleaned_df


# =====================================================
# Main Cleaning Pipeline
# =====================================================

def clean_dataset(df: pd.DataFrame):
    """
    Complete Data Cleaning Pipeline.

    Steps:
    1. Remove duplicate rows
    2. Remove empty rows
    3. Fill missing values
    """

    cleaned_df, duplicate_removed = remove_duplicates(df)

    cleaned_df, empty_rows_removed = remove_empty_rows(cleaned_df)

    cleaned_df = fill_missing_values(cleaned_df)

    return (
        cleaned_df,
        duplicate_removed,
        empty_rows_removed
    )