import pandas as pd
import numpy as np
from utils import get_logger
logger = get_logger()

def preprocess_data(file_path):
    column_names = [
        "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
        "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
    ]
    
    # Load the CSV without headers, assign column names
    df = pd.read_csv(file_path, na_values='?', header=None,names=column_names)
    
    # Convert all columns to numeric
    df = df.apply(pd.to_numeric, errors='coerce')

    # Replace missing values (NaNs) in all numeric columns with their respective column means
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Convert target to binary
    df['target'] = df['target'].apply(lambda x: 1 if x > 0 else 0)

    # Split features and target
    X = df.drop('target', axis=1)
    y = df['target']

    return X, y

if __name__ == "__main__":
    X, y = preprocess_data("../data/processed_cleveland_data.csv")
    logger.info(X.head())
    logger.info(f"Shape: {X.shape}, Label distribution: {y.value_counts().to_dict()}")
