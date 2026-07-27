import streamlit as st

from ui.cleaning import show_cleaning_tools
from modules.auto_clean import auto_clean_dataset


def show_cleaning_page(df):

    st.header("🧹 Data Cleaning Center")

    show_cleaning_tools(df)

if st.button(
    "🧹 Start Auto Cleaning",
    use_container_width=True,
):

    cleaned_df, report = auto_clean_dataset(df)

    st.session_state.df = cleaned_df

    st.success("Dataset cleaned successfully!")

    st.subheader("Cleaning Summary")

    for key, value in report.items():

        st.write(f"✅ **{key}:** {value}")

    csv = cleaned_df.to_csv(index=False)

    st.download_button(
        "⬇ Download Clean Dataset",
        csv,
        "clean_dataset.csv",
        "text/csv",
    )