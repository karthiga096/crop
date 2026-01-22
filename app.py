import streamlit as st
import pandas as pd

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Crop Yield Prediction",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(
    """
    <h1 style='text-align: center; color: green;'>🌽 Crop Yield Prediction 🌽</h1>
    <p style='text-align: center; color: gray;'>Enter the crop and field details below to predict yield.</p>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar upload
# -----------------------------
st.sidebar.header("Upload CSV Dataset")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        st.success("✅ Dataset loaded successfully!")
        st.subheader("Preview of Dataset")
        st.dataframe(data.head())
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        st.stop()
else:
    st.info("Please upload a CSV file to proceed.")
    st.stop()

# -----------------------------
# User input dictionary
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
        # Non-numeric columns → mode
        if not data[col].mode().empty:
            default_value = str(data[col].mode()[0])
        else:
            default_value = ""
        user_input[col] = st.text_input(f"{col}", value=default_value)

# -----------------------------
# Show input values
# -----------------------------
st.markdown("---")
st.subheader("Your Input Values (Real-Time)")
st.json(user_input)

# -----------------------------
# Convert user_input to DataFrame
# -----------------------------
input_df = pd.DataFrame([user_input])
st.subheader("Input as DataFrame")
st.dataframe(input_df.style.background_gradient(cmap='Greens'))

# -----------------------------
# Predict button (placeholder)
# -----------------------------
if st.button("Predict Crop Yield 🌾"):
    # Here you can load your ML model and predict
    # For now, just showing a placeholder
    st.success("Predicted Crop Yield: 62,000 hg/ha ✅")
    st.balloons()  # Fun visual feedback
