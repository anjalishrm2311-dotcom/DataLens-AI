import streamlit as st

from ui.dashboard import show_dashboard
from ui.charts import (
    show_missing_chart,
    show_dtype_chart,
    show_quality_gauge
)
from ui.insights import show_ai_insights


def show_dashboard_page(
    df,
    summary,
    quality_score,
    missing_df,
    duplicate_df,
    email_report,
    insights
):

    # ====================================
    # Executive Dashboard
    # ====================================

    show_dashboard(
        summary,
        quality_score
    )

    show_quality_gauge(
        quality_score
    )

    st.divider()

    # ====================================
    # Data Type Distribution
    # ====================================

    show_dtype_chart(df)

    st.info(f"""
📌 **Quick Insight**

• Numeric Columns : **{summary['Numeric Columns']}**

• Categorical Columns : **{summary['Categorical Columns']}**

This dataset is suitable for exploratory data analysis.
""")

    st.divider()

    # ====================================
    # Missing Value Analysis
    # ====================================

    st.subheader("🚨 Missing Value Analysis")

    show_missing_chart(
        missing_df
    )

    with st.expander("📋 View Missing Value Table"):

        st.dataframe(
            missing_df,
            width="stretch"
        )

    st.divider()

    # ====================================
    # Duplicate Analysis
    # ====================================

    st.subheader("📄 Duplicate Analysis")

    if duplicate_df.empty:

        st.success(
            "✅ No Duplicate Rows Found"
        )

    else:

        st.warning(
            f"⚠ {len(duplicate_df):,} Duplicate Rows Found"
        )

        st.dataframe(
            duplicate_df.head(100),
            width="stretch",
            height=400
        )

    st.divider()

    # ====================================
    # Email Validation
    # ====================================

    st.subheader("📧 Email Validation")

    if email_report.empty:

        st.info(
            "ℹ No Email Column Found"
        )

    else:

        st.dataframe(
            email_report.head(100),
            width="stretch",
            height=400
        )

    st.divider()

    # ====================================
    # AI Insights
    # ====================================

    show_ai_insights(
        insights
    )