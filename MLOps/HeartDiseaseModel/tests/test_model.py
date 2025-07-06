import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from data_preprocessing import preprocess_data
import pandas as pd

def test_data_preprocessing_shape():
    csv_path = os.path.join(os.path.dirname(__file__), "..", "Data", "processed_cleveland_data.csv")
    X, y = preprocess_data(csv_path)

    # Test shape alignment
    assert len(X) == len(y), "Mismatch between X and y lengths"

def test_data_no_missing_values():
    csv_path = os.path.join(os.path.dirname(__file__), "..", "Data", "processed_cleveland_data.csv")
    X, y = preprocess_data(csv_path)

    # Ensure no NaNs remain
    assert not X.isnull().values.any(), "X contains NaN values"
    assert not y.isnull().values.any(), "y contains NaN values"

def test_data_column_names():
    csv_path = os.path.join(os.path.dirname(__file__), "..", "Data", "processed_cleveland_data.csv")
    X, y = preprocess_data(csv_path)

    expected_cols = [
        "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
        "thalach", "exang", "oldpeak", "slope", "ca", "thal"
    ]
    assert list(X.columns) == expected_cols, "Column names don't match"
