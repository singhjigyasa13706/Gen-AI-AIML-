import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("PROJECT 4 Linear Regression/homeprices.csv")

# Train Model
X = df[['area']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Home Price Predictor", page_icon="🏠")

st.title("🏠 Home Price Prediction")
st.write("Predict house price based on area using Linear Regression.")

# User Input
area = st.number_input(
    "Enter Area (Square Feet)",
    min_value=100,
    value=1000,
    step=100
)

if st.button("Predict Price"):
    prediction = model.predict([[area]])[0]

    st.success(f"Estimated House Price: ₹ {prediction:,.2f}")

# -------------------------------
# Display Dataset
# -------------------------------
with st.expander("View Dataset"):
    st.dataframe(df)

# -------------------------------
# Batch Prediction
# -------------------------------
st.subheader("Predict Prices from CSV")

uploaded_file = st.file_uploader(
    "Upload a CSV containing an 'area' column",
    type=["csv"]
)

if uploaded_file is not None:
    test_df = pd.read_csv(uploaded_file)

    if "area" in test_df.columns:
        test_df["Predicted Price"] = model.predict(test_df[["area"]])
        st.dataframe(test_df)

        csv = test_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Predictions",
            data=csv,
            file_name="prediction.csv",
            mime="text/csv",
        )
    else:
        st.error("CSV must contain an 'area' column.")
