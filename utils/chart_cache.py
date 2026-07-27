import streamlit as st
import plotly.express as px


@st.cache_data(show_spinner=False)
def cached_histogram(df, column):

    return px.histogram(
        df,
        x=column
    )


@st.cache_data(show_spinner=False)
def cached_boxplot(df, column):

    return px.box(
        df,
        y=column
    )


@st.cache_data(show_spinner=False)
def cached_bar(df, x, y):

    return px.bar(
        df,
        x=x,
        y=y
    )


@st.cache_data(show_spinner=False)
def cached_scatter(df, x, y):

    return px.scatter(
        df,
        x=x,
        y=y
    )


@st.cache_data(show_spinner=False)
def cached_pie(df, names):

    return px.pie(
        df,
        names=names
    )