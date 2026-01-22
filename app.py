import streamlit as st
import pandas as pd

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Crop Yield Prediction",
    layout="wide"
)

st.markdown(
    """
    <h1 style='text-align: center; color: green;'>🌽 Crop Yield Prediction 🌽</h1>
    <p style='text-align: center; color: gray;'>Enter crop and field details below to predict yield.</p>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Load dataset from local file
# -----------------------------
DATA_PATH = "yield.csv"  # CSV must be in the same folder
try:
    data = pd.read_csv(DATA_PATH)
    st.success("✅ Dataset loaded successfully!")
    st.subheader("Preview of Dataset")
    st.dataframe(data.head())
except FileNotFoundError:
    st.error(f"File '{DATA_PATH}' not found. Please make sure it exists in the project folder.")
    st.stop()

# -----------------------------
# Dynamic user input form
# -----------------------------
user_input = {}
st.subheader("Enter Crop Details")

for col in data.columns:
    if pd.api.types.is_numeric_dtype(data[col]):
        # Use mode for codes or year, mean for continuous numeric
        if "code" in col.lower() or "year" in col.lower():
            default_value = int(data[col].mode()[0])
        else:
            default_value = float(data[col].mean(skipna=True))
        user_input[col] = st.number_input(
            f"{col}",
            value=default_value,
            format="%d" if "code" in col.lower() or "year" in col.lower() else "%.2f"
        )
    else:
        # Non-numeric → mode
        if not data[col].mode().empty:
            default_value = str(data[col].mode()[0])
        else:
            default_value = ""
        user_input[col] = st.text_input(f"{col}", value=default_value)

# -----------------------------
# Show real-time input
# -----------------------------
st.markdown("---")
st.subheader("Your Input Values (Real-Time)")
st.json(user_input)

# -----------------------------
# Convert input to DataFrame
# -----------------------------
input_df = pd.DataFrame([user_input])
st.subheader("Input as DataFrame")
st.dataframe(input_df.style.background_gradient(cmap='Greens'))

# -----------------------------
# Predict button (placeholder)
# -----------------------------
if st.button("Predict Crop Yield 🌾"):
    # Replace this with ML model prediction if available
    st.success("Predicted Crop Yield: 62,000 hg/ha ✅")
    st.balloons()
