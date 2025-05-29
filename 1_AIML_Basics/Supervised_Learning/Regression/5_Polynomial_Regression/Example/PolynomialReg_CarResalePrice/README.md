# 🚗 Car Resale Price Prediction using Polynomial Regression

This project implements a machine learning model to predict used car resale prices using **Polynomial Regression**. It uses feature engineering and a pipeline architecture to handle preprocessing, polynomial expansion, and model training.

## 📂 Files Included

- `car data.csv` – Original CarDekho dataset
- `PolyReg_CarResalePrice_model.pkl` – Trained polynomial regression pipeline
- `README.md` – This file
- `requirements.txt` – List of dependencies

## 📊 Model Highlights

- **Model**: Polynomial Regression (degree 2)
- **Target**: Selling_Price
- **Features used for polynomial expansion**: Present_Price, Car_Age
- **Preprocessing**: StandardScaler for numeric, OneHotEncoder for categoricals
- **R² Score**: ~0.965 ✅
- **MSE**: ~0.81 ✅

## 🛠 How to Run

```bash
# Step 1: Clone this repository
git clone https://github.com/yourusername/car-resale-polynomial.git
cd car-resale-polynomial

# Step 2: Install requirements
pip install -r requirements.txt

# Step 3: Run the notebook or load the model
```

## 🔧 Features Used

- Present_Price
- Kms_Driven
- Owner
- Car_Age (derived from Year)
- Fuel_Type, Seller_Type, Transmission (encoded)

## 💡 Learning Points

- Detecting non-linear relationships with scatter plots
- Using PolynomialFeatures with ColumnTransformer
- Building a pipeline with mixed preprocessing
- Model evaluation and saving


## 👨‍💻 Author

**Sandeep Patil**  
*M.Tech in AI & ML | Automotive Software | Computer Vision | AUTOSAR*

