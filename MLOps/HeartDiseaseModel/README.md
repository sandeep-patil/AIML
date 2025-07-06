
# ❤️ Heart Disease Prediction API

This project provides two interfaces to predict heart disease using a trained machine learning model:
- A **FastAPI** backend (REST API)
- A **Streamlit** frontend (web UI)
- Model training and evaluation pipeline using scikit-learn

---

## 📁 Project Structure

```
.
├── app.py                 # FastAPI application
├── streamlit_app.py       # Streamlit web UI
├── Dockerfile             # Docker setup (for FastAPI)
├── requirements.txt       # Python dependencies
├── model.pkl              # Trained ML model
├── app/
│   ├── main.py            # Model training + evaluation
│   ├── model.py           # Model training logic
│   ├── utils.py           # Logger + model save/load
│   ├── data_preprocessing.py # CSV loading and cleaning
├── tests/                 # Test cases
│   └── test_app.py        # API tests
│   └── test_model.py      # Model tests
```

---

## How to Run

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Train Model (Optional, model already saved)

```bash
python app/main.py
```

---

### 3. Run FastAPI

```bash
uvicorn app:app --reload
```

📍 Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 4. Run Streamlit UI

```bash
streamlit run streamlit_app.py
```

📍 Visit: [http://localhost:8501](http://localhost:8501)

---

## 5. Sample API Call (via cURL)

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{
    "age": 63,
    "sex": 1,
    "cp": 3,
    "trestbps": 145,
    "chol": 233,
    "fbs": 1,
    "restecg": 0,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 2.3,
    "slope": 0,
    "ca": 0,
    "thal": 1
}'
```

Expected response:

```json
{
  "prediction": 1,
  "message": "Heart Disease Detected"
}
```

---

## 6. Docker 

### Build and Run FastAPI Container

```bash
docker build -t heart-disease-api .
docker run -d -p 8000:8000 heart-disease-api
```

---

## 7. Run Tests

```bash
pytest tests/
```

---
