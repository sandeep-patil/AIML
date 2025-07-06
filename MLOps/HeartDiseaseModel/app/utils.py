import joblib
import logging
import os

def save_model(model, filename="model.pkl"):
    joblib.dump(model, filename)
    get_logger().info(f"Model saved as '{filename}'")

def load_model(filename="model.pkl"):
    try:
        model = joblib.load(filename)
        get_logger().info(f"Model loaded from '{filename}'")
        return model
    except FileNotFoundError:
        get_logger().info(f"File '{filename}' not found.")
        return None

def get_logger():
    logger = logging.getLogger("central_logger")
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # File handler
        file_handler = logging.FileHandler("app.log")  # Single centralized log file
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger
