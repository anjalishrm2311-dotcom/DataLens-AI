import streamlit as st

from modules.summary import get_dataset_summary
from modules.missing import analyze_missing_values
from modules.duplicates import analyze_duplicates
from modules.quality_score import calculate_quality_score
from modules.validation import validate_emails
from modules.insights import generate_insights
from modules.profiling import (
    profile_numeric_columns,
    profile_categorical_columns
)
from modules.analytics import (
    calculate_correlation,
    detect_outliers,
    generate_correlation_summary
)

@st.cache_data(show_spinner=False)
def cached_validate_emails(df):
    return validate_emails(df)


@st.cache_data(show_spinner=False)
def cached_generate_insights(
    summary,
    quality_score,
    missing_df,
    duplicate_df
):
    return generate_insights(
        summary,
        quality_score,
        missing_df,
        duplicate_df
    )


@st.cache_data(show_spinner=False)
def cached_numeric_profile(df):
    return profile_numeric_columns(df)


@st.cache_data(show_spinner=False)
def cached_categorical_profile(df):
    return profile_categorical_columns(df)


@st.cache_data(show_spinner=False)
def cached_correlation(df):
    return calculate_correlation(df)


@st.cache_data(show_spinner=False)
def cached_outliers(df):
    return detect_outliers(df)


@st.cache_data(show_spinner=False)
def cached_correlation_summary(correlation_matrix):
    return generate_correlation_summary(correlation_matrix)

@st.cache_data(show_spinner=False)
def cached_summary(df):
    return get_dataset_summary(df)

@st.cache_data(show_spinner=False)
def cached_numeric_columns(df):
    return df.select_dtypes(include="number").columns.tolist()

@st.cache_data(show_spinner=False)
def cached_categorical_columns(df):
    return df.select_dtypes(include="object").columns.tolist()

@st.cache_data(show_spinner=False)
def cached_missing(df):
    return analyze_missing_values(df)


@st.cache_data(show_spinner=False)
def cached_duplicates(df):
    return analyze_duplicates(df)


@st.cache_data(show_spinner=False)
def cached_quality(df):
    return calculate_quality_score(df)

@st.cache_data(show_spinner=False)
def cached_column(df, column):
    return df[[column]].copy()



