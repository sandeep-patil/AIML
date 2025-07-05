from data_preprocessing import preprocess_data
import pandas as pd

def test_data_preprocessing_shape():
    X, y = preprocess_data("data/heart.csv")

    # Test shape alignment
    assert len(X) == len(y), "Mismatch between X and y lengths"

def test_data_no_missing_values():
    X, y = preprocess_data("data/heart.csv")

    # Ensure no NaNs remain
    assert not X.isnull().values.any(), "X contains NaN values"
    assert not y.isnull().values.any(), "y contains NaN values"

def test_data_column_names():
    X, _ = preprocess_data("data/heart.csv")

    expected_cols = [
        "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
        "thalach", "exang", "oldpeak", "slope", "ca", "thal"
    ]
    assert list(X.columns) == expected_cols, "Column names don't match"
