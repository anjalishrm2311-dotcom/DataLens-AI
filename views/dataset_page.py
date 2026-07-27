import streamlit as st
import pandas as pd


def show_dataset_page(df):

    st.header("📂 Dataset Explorer")

    st.write(
        """
        Explore the uploaded dataset, inspect its structure,
        and preview the records.
        """
    )

    st.divider()

    # =====================================
    # Dataset Overview
    # =====================================

    st.subheader("📊 Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", f"{len(df):,}")

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:

        memory = round(
            df.memory_usage(deep=True).sum() /
            (1024 * 1024),
            2
        )

        st.metric("Memory (MB)", memory)

    st.divider()

    # =====================================
    # Search Columns
    # =====================================

    st.subheader("🔍 Search Columns")

    search = st.text_input(
        "Search Column Name"
    )

    if search:

        filtered_columns = [

            col

            for col in df.columns

            if search.lower() in col.lower()

        ]

    else:

        filtered_columns = df.columns.tolist()

    st.write(
        f"Columns Found : {len(filtered_columns)}"
    )

    st.dataframe(

        pd.DataFrame({

            "Columns": filtered_columns

        }),

        width="stretch",
        height=250

    )

    st.divider()

    # =====================================
    # Dataset Preview
    # =====================================

    st.subheader("📄 Dataset Preview")

    preview_rows = st.selectbox(

        "Rows to Preview",

        [10, 50, 100, 500, 1000],

        index=1

    )

    st.dataframe(

        df.head(preview_rows),

        width="stretch",

        height=450

    )

    st.caption(

        f"Showing {min(preview_rows, len(df)):,} "

        f"of {len(df):,} rows"

    )

    st.divider()

    # =====================================
    # Column Information
    # =====================================

    st.subheader("📋 Column Information")

    column_info = pd.DataFrame({

        "Column": df.columns,

        "Data Type": df.dtypes.astype(str),

        "Missing Values": df.isnull().sum().values,

        "Unique Values": df.nunique().values

    })

    st.dataframe(

        column_info,

        width="stretch",

        height=500

    )