import pandas as pd
import numpy as np


# =====================================================
# Calculate Correlation Matrix
# =====================================================

def calculate_correlation(df: pd.DataFrame):
    """
    Calculate Pearson correlation matrix
    for numeric columns.
    """

    numeric_df = df.select_dtypes(
        include="number"
    )

    if numeric_df.empty:
        return pd.DataFrame()

    correlation_matrix = numeric_df.corr(
        method="pearson"
    )

    return correlation_matrix


# =====================================================
# Detect Outliers Using IQR Method
# =====================================================

def detect_outliers(df: pd.DataFrame):
    """
    Detect outliers in numeric columns using the IQR method.

    Outlier rule:
    Value < Q1 - 1.5 * IQR
    Value > Q3 + 1.5 * IQR
    """

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    outlier_data = []

    for column in numeric_columns:

        series = df[column].dropna()

        if series.empty:
            continue

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)

        outliers = series[
            (series < lower_bound)
            | (series > upper_bound)
        ]

        outlier_percentage = (
            len(outliers) / len(series)
        ) * 100

        outlier_data.append({
            "Column": column,
            "Q1": round(q1, 2),
            "Q3": round(q3, 2),
            "IQR": round(iqr, 2),
            "Lower Bound": round(lower_bound, 2),
            "Upper Bound": round(upper_bound, 2),
            "Outlier Count": len(outliers),
            "Outlier %": round(outlier_percentage, 2)
        })

    return pd.DataFrame(outlier_data)


# =====================================================
# Generate Correlation Insights
# =====================================================

def generate_correlation_summary(correlation_matrix):
    """
    Generate automatic insights for strong correlations.
    """

    insights = []

    if correlation_matrix.empty:
        return insights

    columns = correlation_matrix.columns

    for i in range(len(columns)):

        for j in range(i + 1, len(columns)):

            column_1 = columns[i]
            column_2 = columns[j]

            correlation = correlation_matrix.loc[
                column_1,
                column_2
            ]

            if pd.isna(correlation):
                continue

            if correlation >= 0.7:

                insights.append({
                    "Column 1": column_1,
                    "Column 2": column_2,
                    "Correlation": round(correlation, 2),
                    "Relationship": "Strong Positive"
                })

            elif correlation <= -0.7:

                insights.append({
                    "Column 1": column_1,
                    "Column 2": column_2,
                    "Correlation": round(correlation, 2),
                    "Relationship": "Strong Negative"
                })

    return insights