import pandas as pd
import streamlit as st
import time
import zipfile
import io

@st.cache_data(show_spinner=False)
def load_csv(uploaded_file, encoding):
    uploaded_file.seek(0)

    start = time.perf_counter()

    df = pd.read_csv(
        uploaded_file,
        encoding=encoding,
        low_memory=False
    )

    end = time.perf_counter()

    st.write(f"CSV Read Time: {end-start:.2f} seconds")

    return df

@st.cache_data(show_spinner=False)
def load_excel(uploaded_file):
    uploaded_file.seek(0)
    return pd.read_excel(uploaded_file)

st.info(
    "💡 Tip: For faster uploads on slow internet, upload a ZIP file containing your CSV."
)

def upload_dataset():

    uploaded_file = st.file_uploader(
        "📂 Upload Dataset",
        type=["csv", "xlsx", "zip"]
    )

    if uploaded_file is None:
        return None

    try:

        if uploaded_file.name.endswith(".csv"):

            # Show warning for large files
            if uploaded_file.size > 100 * 1024 * 1024:
                st.warning("⚠️ Large dataset detected. Initial loading may take a while.")

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

        elif uploaded_file.name.endswith(".zip"):

            with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
                zip_files = zip_ref.namelist()
                if not zip_files:
                    st.error("ZIP file is empty.")
                    return None

                # Assuming the first file in the ZIP is the one we want to read
                file_name = zip_files[0]
                with zip_ref.open(file_name) as f:
                    if file_name.endswith(".csv"):
                        return load_csv(io.BytesIO(f.read()), "utf-8")
                    elif file_name.endswith(".xlsx"):
                        return load_excel(io.BytesIO(f.read()))

        else:

            with st.spinner("Loading dataset... Please wait ⏳"):
                return load_excel(uploaded_file)

    except Exception as e:

        st.error(f"Error reading file:\n{e}")
        return None