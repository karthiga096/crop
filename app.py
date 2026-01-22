import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("linear_regression_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Crop Yield Prediction App 🌾")

st.write("""
This app predicts crop production based on input features like area, fertilizer, and other factors.
""")

# Load dataset to display (optional)
if st.checkbox("Show dataset"):
    data = pd.read_csv("yield.csv")
    st.dataframe(data.head())

st.header("Enter the values to predict crop production:")

# Dynamically create inputs based on dataset columns (excluding target)
data = pd.read_csv("yield.csv")
input_cols = [col for col in data.columns if col.lower() != "production"]

user_input = {}
for col in input_cols:
    # If column is numeric
    user_input[col] = st.number_input(f"{col}", value=float(data[col].mean()))

# Predict button
if st.button("Predict"):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Crop Production: {prediction:.2f}")
