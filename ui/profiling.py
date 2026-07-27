import streamlit as st
import pandas as pd
import plotly.express as px


from utils.cache import cached_column, cached_numeric_columns

from utils.cache import (
    cached_numeric_profile,
    cached_categorical_profile,
    cached_numeric_columns,
    cached_column
)


def show_profiling(df):

    numeric_profile = cached_numeric_profile(df)

    categorical_profile = cached_categorical_profile(df)

    # -----------------------------
    # Numeric Profiling
    # -----------------------------
    st.subheader("📈 Numeric Columns")

    if numeric_profile.empty:

        st.info("No Numeric Columns Found.")

    else:

        st.dataframe(
            numeric_profile,
            use_container_width=True
        )

        numeric_columns = cached_numeric_columns(df)

        selected_column = st.selectbox(
            "Select Numeric Column",
            numeric_columns
        )
        column_df = cached_column(df, selected_column)
        
        fig = px.histogram(
            column_df,
            x=selected_column,
            title=f"{selected_column} Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
        column_df = cached_column(df, selected_column)

        fig = px.box(
            column_df,
            y=selected_column,
            points="outliers",
            title=f"{selected_column} Box Plot"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # -----------------------------
    # Categorical Profiling
    # -----------------------------
    st.subheader("📝 Categorical Columns")

    if categorical_profile.empty:

        st.info("No Categorical Columns Found.")

    else:

        st.dataframe(
            categorical_profile,
            use_container_width=True
        )