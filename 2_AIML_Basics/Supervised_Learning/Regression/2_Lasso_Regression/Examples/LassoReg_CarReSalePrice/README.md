# 🚗 LassoReg_CarReSalePrice – Used Car Price Prediction with Lasso Regression

Predict the resale value of used cars using a machine learning model trained with **Lasso Regression** and real-world data from CarDekho.

## 📌 Project Overview

- **Goal**: Predict the selling price of used cars
- **Type**: Supervised Regression
- **Algorithm**: Lasso Regression (L1 Regularization)
- **Dataset**: [CarDekho Used Car Dataset](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho)

## 📁 Project Structure

```
LassoReg_CarReSalePrice/
├── LassoReg_CarReSalePrice_model.pkl             # Trained LassoCV model
├── LassoReg_CarReSalePrice_preprocessor.pkl      # Preprocessing pipeline
├── LassoReg_CarReSalePrice_full_pipeline.pkl     # Complete model pipeline (recommended)
├── LassoReg_CarReSalePrice_Model.ipynb           # Jupyter Notebook with full pipeline
├── car data.csv                                  # Dataset used (small <100MB version)
├── README.md                                     # Project documentation (this file)
└── requirements.txt                              # Required Python packages
└── archive.zip                                   # Zipped Dataset from kaggle
└── archive                                       # Unzipped Dataset from kaggle
```

## 📊 Features Used

- Present_Price
- Kms_Driven
- Owner
- Car_Age (derived from Year)
- Fuel_Type (Petrol/Diesel)
- Seller_Type (Dealer/Individual)
- Transmission (Manual/Automatic)

## 🔧 Model Highlights

- **Model**: `LassoCV` with auto-selected alpha
- **Best Alpha**: 0.001
- **R² Score**: ~0.85
- **Feature Selection**: Automatically shrinks irrelevant features to 0
- **Preprocessing**: Includes StandardScaler and OneHotEncoder using ColumnTransformer

## 🚀 How to Use

### ✅ Predict using saved model:

```python
import joblib
import pandas as pd

# Load model pipeline
model = joblib.load("LassoReg_CarReSalePrice_full_pipeline.pkl")

# New car input (must match original feature structure)
new_data = pd.DataFrame([{
    'Present_Price': 6.5,
    'Kms_Driven': 45000,
    'Owner': 1,
    'Car_Age': 5,
    'Fuel_Type': 'Diesel',
    'Seller_Type': 'Individual',
    'Transmission': 'Manual'
}])

# Predict
prediction = model.predict(new_data)
print("Predicted Price (in lakhs ₹):", prediction[0])
```

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 📚 Requirements

- Python 3.8+
- pandas, scikit-learn, joblib, matplotlib

## 📈 Output Example

| Feature               | Coefficient |
|-----------------------|-------------|
| Present_Price         | +3.70       |
| Kms_Driven            | –0.24       |
| Fuel_Type_Diesel      | +2.28       |
| Transmission_Manual   | –1.63       |
| ...                   | ...         |

## 👨‍💻 Author

**Sandeep Patil**  
*M.Tech in AI & ML | Automotive Software | Computer Vision*
