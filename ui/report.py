import streamlit as st

from modules.report import generate_report


def show_report_button(
    summary,
    quality_score,
    missing_df,
    duplicate_df,
    insights,
    memory_usage
):

    filename = "DataLens_Report.pdf"

    if st.button("📄 Generate Professional Audit Report"):

        generate_report(
            summary,
            quality_score,
            missing_df,
            duplicate_df,
            insights,
            memory_usage,
            filename
        )

        with open(filename, "rb") as file:

            st.download_button(
                label="⬇ Download Professional Report",
                data=file,
                file_name=filename,
                mime="application/pdf"
            )