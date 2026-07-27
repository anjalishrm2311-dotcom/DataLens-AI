import streamlit as st
import pandas as pd

from modules.cleaning import clean_dataset


def show_cleaning_tools(df: pd.DataFrame):

    st.write("""
Click below to automatically:

✔ Remove Duplicate Rows

✔ Remove Empty Rows

✔ Fill Missing Values
""")

    if st.button("🧹 Clean Dataset"):

        cleaned_df, duplicates_removed, empty_rows_removed = clean_dataset(df)

        # Store cleaned dataframe
        st.session_state.df = cleaned_df
        st.session_state.cleaned_df = cleaned_df

        st.success("Dataset cleaned successfully!")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Duplicate Rows Removed", duplicates_removed)

        with col2:
            st.metric("Empty Rows Removed", empty_rows_removed)

    # Show cleaned dataset if available
    if "cleaned_df" in st.session_state:

        cleaned_df = st.session_state.cleaned_df

        st.subheader("📄 Cleaned Dataset Preview")

        st.dataframe(
            cleaned_df.head(100),
            use_container_width=True
        )

        csv = cleaned_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇ Download Cleaned Dataset",
            data=csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )