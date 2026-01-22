import streamlit as st
import pandas as pd

# -----------------------------
# Load your dataset
# -----------------------------
DATA_PATH = "yield.csv"  # make sure your CSV is in the same folder
try:
    data = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    st.error(f"File '{DATA_PATH}' not found. Please upload your dataset.")
    st.stop()

st.title("Dynamic Streamlit Form for Dataset Columns")

# -----------------------------
# Create a dictionary to hold user inputs
# -----------------------------
user_input = {}

# -----------------------------
# Loop through all columns in the dataset
# -----------------------------
for col in data.columns:
    if pd.api.types.is_numeric_dtype(data[col]):
        # Numeric columns → use mean as default
        default_value = data[col].mean(skipna=True)
        user_input[col] = st.number_input(f"{col}", value=float(default_value))
    else:
        # Non-numeric columns → use mode (most frequent value) as default
        if not data[col].mode().empty:
            default_value = str(data[col].mode()[0])
        else:
            default_value = ""
        user_input[col] = st.text_input(f"{col}", value=default_value)

# -----------------------------
# Show user inputs
# -----------------------------
st.subheader("Your Input Values")
st.json(user_input)

# -----------------------------
# Optional: You can convert user_input back to DataFrame
# -----------------------------
input_df = pd.DataFrame([user_input])
st.subheader("Input as DataFrame")
st.dataframe(input_df)
