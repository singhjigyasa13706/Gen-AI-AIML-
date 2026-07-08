import streamlit as st
import pandas as pd

st.set_page_config(page_title="Outlier Removal using Percentiles", layout="wide")

st.title("📊 Outlier Removal using Percentiles")
st.write("Upload the **AB_NYC_2019.csv** dataset to remove outliers from the **price** column.")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Original Dataset")
    st.write(df.head())

    if "price" not in df.columns:
        st.error("The uploaded CSV does not contain a 'price' column.")
    else:
        st.subheader("Price Statistics (Before Outlier Removal)")
        st.write(df["price"].describe())

        # Calculate thresholds
        min_threshold, max_threshold = df["price"].quantile([0.01, 0.999])

        st.write(f"**Lower Threshold (1%)** : {min_threshold:.2f}")
        st.write(f"**Upper Threshold (99.9%)** : {max_threshold:.2f}")

        # Remove outliers
        df_clean = df[
            (df["price"] > min_threshold) &
            (df["price"] < max_threshold)
        ]

        st.subheader("Dataset After Removing Outliers")
        st.write(df_clean.head())

        st.write(f"**Original Rows:** {len(df)}")
        st.write(f"**Rows After Removing Outliers:** {len(df_clean)}")

        st.subheader("Price Statistics (After Outlier Removal)")
        st.write(df_clean["price"].describe())

        # Download cleaned dataset
        csv = df_clean.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Cleaned Dataset",
            data=csv,
            file_name="AB_NYC_2019_cleaned.csv",
            mime="text/csv",
        )
else:
    st.info("Please upload a CSV file to begin.")
