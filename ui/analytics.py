import streamlit as st
import plotly.express as px
from utils.cache import (
    cached_column,
    cached_correlation,
    cached_outliers,
    cached_correlation_summary
)

def show_analytics(df):
    """
    Display correlation and outlier analytics.
    """

    # =================================================
    # Calculate Analytics
    # =================================================

    correlation_matrix = cached_correlation(df)

    outlier_report = cached_outliers(df)

    correlation_insights = cached_correlation_summary(
        correlation_matrix
    )

    # =================================================
    # Correlation Analysis
    # =================================================

    st.subheader("🔥 Correlation Analysis")

    if correlation_matrix.empty:

        st.info(
            "No numeric columns available for correlation analysis."
        )

    elif len(correlation_matrix.columns) < 2:

        st.info(
            "At least two numeric columns are required "
            "for correlation analysis."
        )

    else:

        fig = px.imshow(
            correlation_matrix,
            text_auto=".2f",
            aspect="auto",
            title="Numeric Column Correlation Heatmap"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        with st.expander("📋 View Correlation Matrix"):

            st.dataframe(
                correlation_matrix,
                use_container_width=True
            )

    st.divider()

    # =================================================
    # Correlation Insights
    # =================================================

    st.subheader("💡 Correlation Insights")

    if not correlation_insights:

        st.info(
            "No strong correlations were detected."
        )

    else:

        for insight in correlation_insights:

            column_1 = insight["Column 1"]
            column_2 = insight["Column 2"]
            correlation = insight["Correlation"]
            relationship = insight["Relationship"]

            if relationship == "Strong Positive":

                st.success(
                    f"📈 {column_1} and {column_2} have a "
                    f"strong positive correlation of "
                    f"{correlation}."
                )

            else:

                st.warning(
                    f"📉 {column_1} and {column_2} have a "
                    f"strong negative correlation of "
                    f"{correlation}."
                )

    st.divider()

    # =================================================
    # Outlier Analysis
    # =================================================

    st.subheader("📦 Outlier Analysis")

    if outlier_report.empty:

        st.info(
            "No numeric columns available for outlier analysis."
        )

    else:

        st.dataframe(
            outlier_report,
            use_container_width=True
        )

        columns_with_outliers = outlier_report[
            outlier_report["Outlier Count"] > 0
        ]["Column"].tolist()

        if not columns_with_outliers:

            st.success(
                "🎉 No potential outliers detected using the IQR method."
            )

        else:

            selected_column = st.selectbox(
                "Select Column for Outlier Visualization",
                columns_with_outliers,
                key="outlier_column"
            )

            column_df = cached_column(df, selected_column)

            fig = px.box(
                column_df,
                y=selected_column,
                points="outliers",
                title=f"{selected_column} - Outlier Analysis"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            selected_report = outlier_report[
                outlier_report["Column"] == selected_column
            ].iloc[0]

            st.info(
                f"""
**Outlier Insight**

Column **{selected_column}** contains
**{selected_report['Outlier Count']} potential outliers**.

Outlier Percentage:
**{selected_report['Outlier %']}%**

Values below **{selected_report['Lower Bound']}**
or above **{selected_report['Upper Bound']}**
are flagged by the IQR method.

⚠️ Potential outliers should be investigated before removal.
"""
            )