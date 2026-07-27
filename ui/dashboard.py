import streamlit as st
from modules import summary
from ui.components import kpi_card


def show_dashboard(summary, quality_score):
    """
    Displays the Executive Dashboard.
    """

    st.markdown(
        """
    # 📊 Executive Dashboard

    Monitor your dataset quality at a glance.
    """
    )

    # -----------------------------
    # Decide Status
    # -----------------------------
    if quality_score >= 90:
        status = "🟢 Excellent"
    elif quality_score >= 75:
        status = "🟢 Good"
    elif quality_score >= 60:
        status = "🟡 Fair"
    else:
        status = "🔴 Poor"

    # -----------------------------
    # KPI Cards
    # -----------------------------
    col1, col2, col3, col4 = st.columns(4)      

    with col1:
        kpi_card(
            "Rows",
            f"{summary['Rows']:,}",
            "📊",
            "#2563EB",
        )

    with col2:
        kpi_card(
            "Columns",
            f"{summary['Columns']:,}",
            "📑",
            "#7C3AED",
        )

    with col3:
        kpi_card(
            "Missing Values",
            f"{summary['Missing Values']:,}",
            "⚠️",
            "#F59E0B",
        )

    with col4:
        kpi_card(
            "Duplicate Rows",
            f"{summary['Duplicate Rows']:,}",
            "📄",
            "#EF4444",
        )

    st.divider()

    # -----------------------------
    # Quality Score
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        kpi_card(
            "Quality Score",
            f"{quality_score}/100",
            "⭐",
         "#10B981",
        )

    with col2:
        kpi_card(
            "Status",
            status,
            "🏆",
            "#06B6D4",
        )