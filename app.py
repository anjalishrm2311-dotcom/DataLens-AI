import streamlit as st
import time

from views.dashboard_page import show_dashboard_page
from views.dataset_page import show_dataset_page
from views.profiling_page import show_profiling_page
from views.analytics_page import show_analytics_page
from views.cleaning_page import show_cleaning_page
from views.report_page import show_report_page
from views.about_page import show_about_page
# =============================
# Modules
# =============================
from modules.upload import upload_dataset
from utils.cache import (
    cached_summary,
    cached_missing,
    cached_duplicates,
    cached_quality,
    cached_validate_emails,
    cached_generate_insights
)

from utils.performance import (
    is_large_dataset,
    sample_dataframe
)

# ====================================
# Page Configuration
# ====================================

st.set_page_config(
    page_title="DataLens",
    page_icon="📊",
    layout="wide"
)

from pathlib import Path

def load_css():

    css_path = Path("assets/style.css")

    if css_path.exists():

        st.markdown(
            f"<style>{css_path.read_text()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.sidebar.image(
    "assets/logo.png",
    width=80
)

st.sidebar.markdown(
    """
# 📊 DataLens AI

**Intelligent Data Quality Audit Platform**

Version **1.0**
"""
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Dataset",
        "Profiling",
        "Analytics",
        "Cleaning",
        "Reports",
        "About"
    ]
)


# ====================================
# Header
# ====================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#2563EB,#7C3AED);
padding:35px;
border-radius:18px;
text-align:center;
color:white;
">

<h1>📊 DataLens AI</h1>

<h3>Intelligent Data Quality Audit Platform</h3>

<p style="font-size:18px;">
Analyze • Clean • Validate • Generate Professional Reports
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("📈\n\n**Data Profiling**")

with col2:
    st.info("🤖\n\n**AI Insights**")

with col3:
    st.info("🧹\n\n**Cleaning**")

with col4:
    st.info("📄\n\n**PDF Reports**")

c1, c2, c3, c4 = st.columns(4)

c1.success("✔ CSV")

c2.success("✔ Excel")

c3.success("✔ Large Datasets")

c4.success("✔ AI Powered")


# ====================================
# Session State Initialization
# ====================================

if "df" not in st.session_state:
    st.session_state.df = None

analysis_keys = [
    "summary",
    "missing_df",
    "duplicate_df",
    "quality_score",
    "email_report",
    "insights"
]

for key in analysis_keys:
    if key not in st.session_state:
        st.session_state[key] = None
        
def get_summary(df):
    if st.session_state.summary is None:
        st.session_state.summary = cached_summary(df)
    return st.session_state.summary


def get_missing(df):
    if st.session_state.missing_df is None:
        st.session_state.missing_df = cached_missing(df)
    return st.session_state.missing_df


def get_duplicates(df):
    if st.session_state.duplicate_df is None:
        st.session_state.duplicate_df = cached_duplicates(df)
    return st.session_state.duplicate_df


def get_quality(df):
    if st.session_state.quality_score is None:
        st.session_state.quality_score = cached_quality(df)
    return st.session_state.quality_score


def get_email_report(df):
    if st.session_state.email_report is None:
        st.session_state.email_report = cached_validate_emails(df)
    return st.session_state.email_report


def get_insights(df):
    if st.session_state.insights is None:

        summary = get_summary(df)
        quality = get_quality(df)
        missing = get_missing(df)
        duplicates = get_duplicates(df)

        st.session_state.insights = cached_generate_insights(
            summary,
            quality,
            missing,
            duplicates
        )

    return st.session_state.insights
# ====================================
# Upload Dataset
# ====================================

start_upload = time.perf_counter()

uploaded_df = upload_dataset()

st.write(f"After upload: {time.perf_counter() - start_upload:.2f} seconds")

if uploaded_df is not None:

    # Only update if a different DataFrame object is uploaded
    if uploaded_df is not st.session_state.df:

        st.session_state.df = uploaded_df

        # Clear previous analysis
        for key in analysis_keys:
            st.session_state[key] = None

df = st.session_state.df
start = time.perf_counter()

if df is None:

    st.markdown("# 📊 Welcome to DataLens AI")

    st.markdown("""
Analyze your datasets with AI-powered data quality auditing.

### Features

- 📈 Data Profiling
- 🚨 Missing Value Detection
- 📄 Duplicate Analysis
- 🤖 AI Insights
- 🧹 Data Cleaning
- 📑 Professional PDF Reports

Upload a CSV or Excel file above to get started.
""")

    st.stop()

# ====================================
# Large Dataset Mode
# ====================================

if df is not None and is_large_dataset(df):

    st.warning(
        f"""
⚠ Large Dataset Mode Enabled

Rows : {len(df):,}

To improve performance,
charts will use a sampled dataset,
while all quality calculations will
still use the complete dataset.
"""
    )

# ====================================
# Run only if dataset exists
# ====================================

if df is not None:

    st.success(
        f"""
        ✅ Dataset Loaded Successfully

        Rows : {len(df):,}

        Columns : {df.shape[1]}
        """
    )

    # ====================================
    # Sidebar Dataset Info
    # ====================================

    st.sidebar.divider()

    st.sidebar.markdown("### 📂 Dataset Information")

    st.sidebar.metric(
        "Rows",
        f"{len(df):,}"
    )

    st.sidebar.metric(
        "Columns",
        df.shape[1]
    )

    st.sidebar.divider()
    # ====================================
    # Sidebar Navigation
    # ====================================

    if page == "Dashboard":

        if st.session_state.summary is None:

            with st.spinner("Analyzing dataset..."):

                st.session_state.summary = cached_summary(df)
                st.session_state.missing_df = cached_missing(df)
                st.session_state.duplicate_df = cached_duplicates(df)
                st.session_state.quality_score = cached_quality(df)
                st.session_state.email_report = cached_validate_emails(df)

                st.session_state.insights = cached_generate_insights(
                    st.session_state.summary,
                    st.session_state.quality_score,
                    st.session_state.missing_df,
                    st.session_state.duplicate_df
                )

        start = time.perf_counter()
        summary = get_summary(df)
        st.write(f"Summary Time: {time.perf_counter()-start:.2f}s")

        start = time.perf_counter()
        missing_df = get_missing(df)
        st.write(f"Missing Time: {time.perf_counter()-start:.2f}s")

        start = time.perf_counter()
        duplicate_df = get_duplicates(df)
        st.write(f"Duplicate Time: {time.perf_counter()-start:.2f}s")

        start = time.perf_counter()
        quality_score = get_quality(df)
        st.write(f"Quality Score Time: {time.perf_counter()-start:.2f}s")

        start = time.perf_counter()
        email_report = get_email_report(df)
        st.write(f"Email Validation Time: {time.perf_counter()-start:.2f}s")

        start = time.perf_counter()
        insights = get_insights(df)
        st.write(f"Insights Time: {time.perf_counter()-start:.2f}s")

        # show_dashboard_page(
        #     df,
        #     summary,
        #     quality_score,
        #     missing_df,
        #     duplicate_df,
        #     email_report,
        #     insights
        # )
        st.success("Dashboard reached successfully")
    elif page == "Profiling":

        analysis_df = sample_dataframe(df)
        show_profiling_page(analysis_df)

    elif page == "Analytics":

        analysis_df = sample_dataframe(df)
        show_analytics_page(analysis_df)

    elif page == "Cleaning":
        show_cleaning_page(df)

    elif page == "Dataset":
        show_dataset_page(df)

    elif page == "About":
        show_about_page()

    elif page == "Reports":

        with st.spinner("Preparing Report..."):

            summary = get_summary(df)
            missing_df = get_missing(df)
            duplicate_df = get_duplicates(df)
            quality_score = get_quality(df)
            email_report = get_email_report(df)
            insights = get_insights(df)

            memory_usage = round(
                df.memory_usage(deep=True).sum() / (1024 * 1024),
                2
            )

        show_report_page(
            summary,
            quality_score,
            missing_df,
            duplicate_df,
            insights,
            memory_usage
        )

st.divider()

st.sidebar.markdown("---")

st.sidebar.caption("© 2026 DataLens AI")

st.sidebar.caption("Developed by Anjali")

st.sidebar.caption("Powered by Streamlit") 