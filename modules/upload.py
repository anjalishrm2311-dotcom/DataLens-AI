import pandas as pd
import streamlit as st


@st.cache_data(show_spinner=False)
def load_csv(uploaded_file, encoding):
    uploaded_file.seek(0)
    return pd.read_csv(
        uploaded_file,
        encoding=encoding,
        low_memory=False
    )


@st.cache_data(show_spinner=False)
def load_excel(uploaded_file):
    uploaded_file.seek(0)
    return pd.read_excel(uploaded_file)


def upload_dataset():

    uploaded_file = st.file_uploader(
        "📂 Upload Dataset",
        type=["csv", "xlsx"]
    )

    if uploaded_file is None:
        return None

    try:

        if uploaded_file.name.endswith(".csv"):

            encodings = [
                "utf-8",
                "latin1",
                "ISO-8859-1",
                "cp1252"
            ]

            for encoding in encodings:

                try:
                    with st.spinner("Loading dataset... Please wait ⏳"):
                    return load_csv(uploaded_file, encoding)

                except UnicodeDecodeError:
                    continue

            st.error("Unable to read CSV. Unsupported encoding.")
            return None

        else:

            with st.spinner("Loading dataset... Please wait ⏳"):
            return load_excel(uploaded_file)

    except Exception as e:

        st.error(f"Error reading file:\n{e}")

        return None