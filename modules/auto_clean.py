import pandas as pd


def auto_clean_dataset(df):

    cleaned = df.copy()

    report = {}

    # -------------------------
    # Remove Duplicates
    # -------------------------

    before = len(cleaned)

    cleaned = cleaned.drop_duplicates()

    report["Duplicates Removed"] = before - len(cleaned)

    # -------------------------
    # Remove Empty Rows
    # -------------------------

    before = len(cleaned)

    cleaned = cleaned.dropna(how="all")

    report["Empty Rows Removed"] = before - len(cleaned)

    # -------------------------
    # Fill Missing Values
    # -------------------------

    missing_before = cleaned.isna().sum().sum()

    for col in cleaned.columns:

        if cleaned[col].dtype == "object":

            cleaned[col] = cleaned[col].fillna("Unknown")

        else:

            cleaned[col] = cleaned[col].fillna(
                cleaned[col].median()
            )

    report["Missing Values Filled"] = missing_before

    # -------------------------
    # Trim Spaces
    # -------------------------

    text_cols = cleaned.select_dtypes(
        include="object"
    ).columns

    for col in text_cols:

        cleaned[col] = cleaned[col].astype(str).str.strip()

    report["Text Columns Cleaned"] = len(text_cols)

    return cleaned, report