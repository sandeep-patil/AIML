from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("logistic_model.pkl")

# Create FastAPI app instance
app = FastAPI(title="Heart Disease Prediction API")

# Define expected input structure using Pydantic
class PatientData(BaseModel):
    age: float
    sex: float
    cp: float
    trestbps: float
    chol: float
    fbs: float
    restecg: float
    thalach: float
    exang: float
    oldpeak: float
    slope: float
    ca: float
    thal: float

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Heart Disease Prediction API is running!"}

# Prediction endpoint
@app.post("/predict")
def predict(data: PatientData):
    features = np.array([[ 
        data.age, data.sex, data.cp, data.trestbps, data.chol, data.fbs,
        data.restecg, data.thalach, data.exang, data.oldpeak, data.slope,
        data.ca, data.thal
    ]])
    
    prediction = model.predict(features)[0]
    result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"
    return {"prediction": int(prediction), "message": result}
