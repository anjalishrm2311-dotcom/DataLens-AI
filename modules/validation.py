import pandas as pd
import re


def validate_emails(df: pd.DataFrame):

    email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    invalid_emails = []

    for column in df.columns:

        if "email" in column.lower():

            invalid = df[
                ~df[column]
                .fillna("")
                .astype(str)
                .str.match(email_pattern)
            ]

            invalid_emails.append(
                {
                    "Column": column,
                    "Invalid Count": len(invalid)
                }
            )

    return pd.DataFrame(invalid_emails)