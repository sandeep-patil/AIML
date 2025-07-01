from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

# Initialize app
app = FastAPI(title="Fuel Efficiency Predictor")

# Input data format
class FuelInput(BaseModel):
    horsepower: float
    weight: float
    acceleration: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fuel Efficiency Predictor API"}


@app.post("/predict")
def predict(data: FuelInput):
    try:
        input_array = np.array([[ 
            data.horsepower,
            data.weight,
            data.acceleration
        ]])
        print("Input:", input_array)  # <-- Debug log
        prediction = model.predict(input_array)
        print("Prediction:", prediction)  # <-- Debug log
        return {"mpg_prediction": round(prediction[0], 2)}
    except Exception as e:
        print("Error:", str(e))  # <-- Show actual error
        return {"error": str(e)}

