import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Google Play Store Data Visualization", layout="wide")

st.title("📊 Google Play Store Data Visualization")
st.write("Interactive dashboard using Streamlit")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("PROJECT 1 Data Visualisation/googleplaystore_v2.csv")

df = load_data()

# Show dataset
if st.checkbox("Show Dataset"):
    st.dataframe(df)

st.sidebar.header("Visualization")

option = st.sidebar.selectbox(
    "Choose a Chart",
    [
        "Ratings Distribution",
        "Content Rating Count",
        "Reviews Histogram",
        "Price Histogram"
    ]
)

if option == "Ratings Distribution":
    fig, ax = plt.subplots()
    df["Rating"].dropna().hist(bins=20, ax=ax)
    ax.set_title("Distribution of Ratings")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

elif option == "Content Rating Count":
    fig, ax = plt.subplots()
    df["Content Rating"].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Content Rating")
    st.pyplot(fig)

elif option == "Reviews Histogram":
    fig, ax = plt.subplots()
    df["Reviews"].dropna().hist(bins=30, ax=ax)
    ax.set_title("Reviews Distribution")
    st.pyplot(fig)

elif option == "Price Histogram":
    fig, ax = plt.subplots()
    df["Price"].dropna().hist(bins=20, ax=ax)
    ax.set_title("Price Distribution")
    st.pyplot(fig)

st.sidebar.markdown("---")
st.sidebar.write("Created using Streamlit")
