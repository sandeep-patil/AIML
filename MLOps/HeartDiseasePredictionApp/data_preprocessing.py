import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def preprocess_data(file_path):
    column_names = [
        "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
        "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
    ]
    
    # Load the CSV without headers, assign column names
    df = pd.read_csv(file_path, header=None, names=column_names)

    # Replace '?' with NaN
    df.replace('?', np.nan, inplace=True)

    # Convert all columns to numeric
    df = df.apply(pd.to_numeric, errors='coerce')

    # Drop rows with any NaNs
    df.dropna(inplace=True)

    # Convert target to binary
    df['target'] = df['target'].apply(lambda x: 1 if x > 0 else 0)

    # Split features and target
    X = df.drop('target', axis=1)
    y = df['target']

    return X, y

if __name__ == "__main__":
    X, y = preprocess_data("data/heart.csv")
    print(X.head())
    print(f"Shape: {X.shape}, Label distribution: {y.value_counts().to_dict()}")
