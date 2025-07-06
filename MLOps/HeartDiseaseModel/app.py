from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import sys
import os
from contextlib import asynccontextmanager

# Dynamically add the "app" folder to Python's module search path
sys.path.append(os.path.join(os.path.dirname(__file__), "app"))

from utils import get_logger
logger = get_logger()

# Load model.pkl from the same directory as app.py
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)
logger.info("Model.pkl loaded successfully")

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

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("FastAPI app started and ready to receive requests.")
    yield
    logger.info("FastAPI app shutting down.")

app = FastAPI(lifespan=lifespan)

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
    logger.info(f"Prediction result: {result}")
    return {"prediction": int(prediction), "message": result}


