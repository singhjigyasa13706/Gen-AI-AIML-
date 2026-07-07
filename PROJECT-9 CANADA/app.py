import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("Canada Per Capita Income Prediction")

# Load dataset
df = pd.read_csv("PROJECT-3 CANADA/PROJECT--3-CANADA--main/canada_per_capita_income.csv")

# Train model
X = df[['year']]
y = df['per capita income (US$)']

model = LinearRegression()
model.fit(X, y)

st.subheader("Dataset")
st.dataframe(df)

# Plot
fig, ax = plt.subplots()
ax.scatter(df.year, y, color="blue", label="Data")
ax.plot(df.year, model.predict(X), color="red", label="Regression Line")
ax.set_xlabel("Year")
ax.set_ylabel("Per Capita Income")
ax.legend()
st.pyplot(fig)

st.subheader("Predict Income")

year = st.number_input(
    "Enter Year",
    min_value=1970,
    max_value=2100,
    value=2020,
    step=1
)

prediction = model.predict([[year]])[0]

st.success(f"Predicted Per Capita Income in {year}: ${prediction:.2f}")

if st.button("Predict 2020"):
    pred2020 = model.predict([[2020]])[0]
    st.info(f"Prediction for 2020: ${pred2020:.2f}")
