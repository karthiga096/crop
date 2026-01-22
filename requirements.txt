import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 Crop Yield Prediction System")
st.write("Predict crop production using Machine Learning (Linear Regression)")

# -----------------------------
# Load and Prepare Dataset
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("crop.csv")
    df = df.dropna()

    # Keep only numeric columns
    df = df.select_dtypes(include=["number"])

    return df

data = load_data()

# Target and Features
y = data["Production"]
X = data.drop("Production", axis=1)

# Train model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# User Input Section
# -----------------------------
st.subheader("🧾 Enter Crop Details")

user_input = {}

for col in X.columns:
    user_input[col] = st.number_input(
        f"{col}",
        min_value=0.0,
        value=float(X[col].mean())
    )

input_df = pd.DataFrame([user_input])

# -----------------------------
# Prediction
# -----------------------------
if st.button("🌱 Predict Crop Yield"):
    prediction = model.predict(input_df)[0]
    st.success(f"✅ Predicted Crop Production: **{prediction:.2f}**")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Mini Project | CropYieldML using Linear Regression")

