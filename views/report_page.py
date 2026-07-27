import streamlit as st

from ui.report import show_report_button


def show_report_page(
    summary,
    quality_score,
    missing_df,
    duplicate_df,
    insights,
    memory_usage
):

    show_report_button(
        summary,
        quality_score,
        missing_df,
        duplicate_df,
        insights,
        memory_usage
    )

    st.header("📄 Professional Audit Report")

    st.write(
        """
Generate a professional Data Quality Audit Report
containing dataset summary, quality assessment,
missing value analysis, duplicate analysis,
AI insights, and recommendations.
"""
    )

    