import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # ✅ Now this will work correctly
from fastapi.testclient import TestClient

client = TestClient(app)
def test_predict_valid_input():
    # Sample input from the UCI heart disease dataset
    sample_input = {
        "age": 60,
        "sex": 1,
        "cp": 3,
        "trestbps": 130,
        "chol": 250,
        "fbs": 0,
        "restecg": 1,
        "thalach": 140,
        "exang": 0,
        "oldpeak": 1.5,
        "slope": 2,
        "ca": 0,
        "thal": 2
    }

    response = client.post("/predict", json=sample_input)
    
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] in [0, 1]
    assert isinstance(response.json()["message"], str)

def test_predict_missing_field():
    # 'age' field is intentionally left out
    invalid_input = {
        # "age": 60,
        "sex": 1,
        "cp": 3,
        "trestbps": 130,
        "chol": 250,
        "fbs": 0,
        "restecg": 1,
        "thalach": 140,
        "exang": 0,
        "oldpeak": 1.5,
        "slope": 2,
        "ca": 0,
        "thal": 2
    }

    response = client.post("/predict", json=invalid_input)
    
    # FastAPI should reject this with status 422 (Unprocessable Entity)
    assert response.status_code == 422

def test_predict_invalid_datatype():
    # 'age' is a string instead of float
    invalid_input = {
        "age": "sixty",
        "sex": 1,
        "cp": 3,
        "trestbps": 130,
        "chol": 250,
        "fbs": 0,
        "restecg": 1,
        "thalach": 140,
        "exang": 0,
        "oldpeak": 1.5,
        "slope": 2,
        "ca": 0,
        "thal": 2
    }

    response = client.post("/predict", json=invalid_input)
    assert response.status_code == 422
