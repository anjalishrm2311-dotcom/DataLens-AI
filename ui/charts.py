import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from ui.chart_theme import apply_theme


# =====================================================
# Missing Value Bar Chart
# =====================================================

def show_missing_chart(missing_df):
    """
    Display Missing Values Bar Chart
    """

    chart_df = missing_df[missing_df["Missing Count"] > 0]

    if chart_df.empty:
        st.success("🎉 No Missing Values Found!")
        return

    chart_df = chart_df.sort_values(
        by="Missing Count",
        ascending=True
    )

    fig = px.bar(
        chart_df,
        x="Missing Count",
        y="Column",
        orientation="h",
        title="Missing Values by Column",
        text="Missing Count",
        color_discrete_sequence=["#F59E0B"]
    )

    fig.update_traces(
        hovertemplate=
        "<b>%{y}</b><br>"
        "Missing Values: %{x:,}<extra></extra>"
    )

    fig.update_layout(
        height=450,
        xaxis_title="Missing Values",
        yaxis_title="Columns",
        template="plotly_white"
    )

    fig = apply_theme(fig)

    st.plotly_chart(
        fig,
        width="stretch"
    )


# =====================================================
# Data Type Distribution Pie Chart
# =====================================================

def show_dtype_chart(df):
    """
    Display Data Type Distribution
    """

    dtype_counts = (
        df.dtypes
        .astype(str)
        .value_counts()
        .reset_index()
    )

    dtype_counts.columns = [
        "Data Type",
        "Count"
    ]

    fig = px.pie(
        names=dtype_counts["Data Type"],
        values=dtype_counts["Count"],
        color_discrete_sequence=[
            "#2563EB",   # Blue
            "#10B981",   # Green
            "#7C3AED",   # Purple
            "#06B6D4",   # Cyan
            "#F59E0B",   # Orange
            "#EF4444"    # Red
        ]
   )

    fig.update_layout(
        template="plotly_white",
        height=450,
        legend_title="Data Types"
    )

    fig.update_traces(
        textinfo="percent+label",
        hovertemplate=
        "<b>%{label}</b><br>"
        "%{value} Columns<extra></extra>"
    )

    fig = apply_theme(fig)

    fig.update_layout(
        transition_duration=500
    )

    st.container(border=True)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# Quality Score Gauge
# =====================================================

def show_quality_gauge(score):
    """
    Display Quality Score Gauge
    """

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,

            title={
                "text": "Overall Quality Score"
            },

            gauge={
                "axis": {
                    "range": [0, 100]
                },

                "bar": {
                    "color": "#10B981"
                },

                "steps": [
                    {"range": [0, 60], "color": "#FEE2E2"},
                    {"range": [60, 80], "color": "#FEF3C7"},
                    {"range": [80, 100], "color": "#DCFCE7"}
                ]
            }
        )
    )

    fig.update_layout(
        height=420
    )

    fig = apply_theme(fig)

    fig.update_layout(
        transition_duration=500
    )

    st.container(border=True)

    st.plotly_chart(
        fig,
        use_container_width=True
    )