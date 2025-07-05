import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("logistic_model.pkl")

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

st.title("❤️ Heart Disease Prediction App")

# Input form
with st.form("heart_form"):
    age = st.number_input("Age", 1, 120, 60)
    sex = st.selectbox("Sex", [0, 1])
    cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure", 80, 200, 130)
    chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 250)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.selectbox("Resting ECG (0–2)", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate Achieved", 60, 250, 150)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression", 0.0, 10.0, 1.0, step=0.1)
    slope = st.selectbox("Slope of ST Segment", [0, 1, 2])
    ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia (1=Fixed, 2=Normal, 3=Reversible)", [1, 2, 3])

    submitted = st.form_submit_button("Predict")

    if submitted:
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                                thalach, exang, oldpeak, slope, ca, thal]])
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.error("🔴 High Risk: Heart Disease Detected!")
        else:
            st.success("🟢 Low Risk: No Heart Disease Detected.")
