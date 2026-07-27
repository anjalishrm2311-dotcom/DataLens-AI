import pandas as pd


def generate_insights(summary, quality_score, missing_df, duplicate_df):

    insights = []

    insights.append(
        f"The dataset contains {summary['Rows']} rows and {summary['Columns']} columns."
    )

    insights.append(
        f"The overall data quality score is {quality_score}/100."
    )

    if summary["Missing Values"] == 0:
        insights.append(
            "No missing values were found."
        )
    else:
        insights.append(
            f"There are {summary['Missing Values']} missing values that should be reviewed."
        )
    if not missing_df.empty:

        worst = missing_df.iloc[0]

        insights.append(
            f"The column '{worst['Column']}' has the highest missing percentage ({worst['Missing Percentage']}%)."
        )
        
    if duplicate_df.empty:
        insights.append(
            "No duplicate rows were detected."
        )
    else:
        insights.append(
            f"{len(duplicate_df)} duplicate rows were detected."
        )

    if quality_score >= 90:
        insights.append(
            "Overall dataset quality is excellent."
        )
    elif quality_score >= 75:
        insights.append(
            "Overall dataset quality is good."
        )
    elif quality_score >= 60:
        insights.append(
            "Dataset quality is average and would benefit from cleaning."
        )
    else:
        insights.append(
            "Dataset quality is poor and significant cleaning is recommended."
        )

    return insights