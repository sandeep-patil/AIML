import streamlit as st
import numpy as np
import joblib
import sys
import os

# Dynamically add the app/ folder to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), "app"))

from utils import get_logger
logger = get_logger()

# Load trained model
model = joblib.load("model.pkl")
logger.info("Streamlit app launched.")
st.title("❤️ Heart Disease Prediction App")

st.write("Enter the patient information below:")

# Mapping for user-friendly options
cp_dict = {
    "Typical Angina (1)": 1,
    "Atypical Angina (2)": 2,
    "Non-anginal Pain (3)": 3,
    "Asymptomatic (4)": 4
}

sex_dict = {
    "Female (0)": 0,
    "Male (1)": 1
}

fbs_dict = {
    "False (0)": 0,
    "True (1)": 1
}

restecg_dict = {
    "Normal (0)": 0,
    "ST-T abnormality (1)": 1,
    "Left ventricular hypertrophy (2)": 2
}

slope_dict = {
    "Upsloping (1)": 1,
    "Flat (2)": 2,
    "Downsloping (3)": 3
}

thal_dict = {
    "Normal (3)": 3,
    "Fixed Defect (6)": 6,
    "Reversible Defect (7)": 7
}

# User input form
age = st.number_input("Age", min_value=1, max_value=120)
sex = sex_dict[st.selectbox("Sex", list(sex_dict.keys()))]
cp = cp_dict[st.selectbox("Chest Pain Type", list(cp_dict.keys()))]
trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=200)
chol = st.number_input("Serum Cholestoral in mg/dl", min_value=100, max_value=600)
fbs = fbs_dict[st.selectbox("Fasting Blood Sugar > 120 mg/dl?", list(fbs_dict.keys()))]
restecg = restecg_dict[st.selectbox("Resting ECG Results", list(restecg_dict.keys()))]
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=250)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=10.0, step=0.1)
slope = slope_dict[st.selectbox("Slope of Peak Exercise ST", list(slope_dict.keys()))]
ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3])
thal = thal_dict[st.selectbox("Thalassemia", list(thal_dict.keys()))]

# Predict button
if st.button("Predict"):
    features = np.array([[age, sex, cp, trestbps, chol, fbs,
                          restecg, thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(features)[0]
    
    if prediction == 1:
        st.error("🔴 High Risk: Heart Disease Detected!")
    else:
        st.success("🟢 Low Risk: No Heart Disease Detected.")
