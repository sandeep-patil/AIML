# Car Resale Price Prediction using Ridge Regression

This repository contains a Ridge Regression-based machine learning model to predict car resale prices. The model helps understand how vehicle features affect resale value and uses Ridge regularization to prevent overfitting.

## 📌 Features

- Ridge Regression with fixed alpha and RidgeCV (cross-validated alpha selection)
- Visualization of feature coefficients
- Model saving for deployment
- Evaluation using R² score and Mean Squared Error (MSE)

## 📂 File Structure

- `RidgeReg_CarResalePrice.ipynb` - Jupyter notebook with complete model code and analysis
- `requirements.txt` - List of dependencies
- `README.md` - This file

## 🛠️ Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/car-resale-ridge.git
   cd car-resale-ridge
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Open the notebook:
   ```bash
   jupyter notebook RidgeReg_CarResalePrice.ipynb
   ```

## 📊 Output Highlights

- Best alpha value using `RidgeCV`
- Plot of actual vs. predicted prices
- Feature importance via Ridge coefficients

## 💾 Model Deployment

Model is saved using joblib and can be loaded for deployment:
```python
import joblib
model = joblib.load("ridge_model.pkl")
```

## 👨‍💻 Author

**Sandeep Patil**  
*M.Tech in AI & ML | Automotive Software | Computer Vision*
