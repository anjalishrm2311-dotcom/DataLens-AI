import streamlit as st

from ui.profiling import show_profiling


def show_profiling_page(df):

    st.header("📊 Data Profiling")

    show_profiling(df)