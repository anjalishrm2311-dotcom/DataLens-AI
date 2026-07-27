import streamlit as st

from ui.analytics import show_analytics


def show_analytics_page(df):

    st.header("📈 Advanced Analytics")

    show_analytics(df)