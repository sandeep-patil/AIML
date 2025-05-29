
# 🚗 Car Resale Price Prediction using Gradient Boosting Regressor

This project builds a Gradient Boosting Regression model to predict car resale prices using the CarDekho dataset. It uses a sequence of shallow decision trees where each tree learns to correct the errors made by the previous one.

## 📁 Files Included

- `car data.csv` – Dataset used for training
- `GradientBoostingReg_CarResalePrice.ipynb` – Complete notebook with preprocessing, GridSearchCV, and evaluation
- `GradientBoostingCarPriceModel.pkl` – Trained Gradient Boosting model
- `README.md` – This file
- `requirements.txt` – Required Python packages

## 🔧 Model Summary

- **Model**: Gradient Boosting Regressor
- **Best Parameters** (via GridSearchCV):
  - `n_estimators = 150`
  - `learning_rate = 0.1`
  - `max_depth = 2`
- **Handles Non-Linearity**: ✅ Yes
- **Handles Categorical Features**: ✅ Yes (via one-hot encoding)
- **Feature Scaling Required**: ❌ No
- **Final R² Score**: ~0.89 on test set
- **Final MSE**: Low

## 🛠 How to Run

```bash
# Step 1: Clone the repo
git clone https://github.com/yourusername/car-resale-gradientboosting.git
cd car-resale-gradientboosting

# Step 2: Install requirements
pip install -r requirements.txt

# Step 3: Run the notebook or load the saved model
```

## 🧠 Features Used

- Year, Present_Price, Kms_Driven, Owner
- Fuel_Type, Seller_Type, Transmission (One-hot encoded)

## 📈 Highlights

- GridSearchCV used for hyperparameter tuning
- Feature importance visualized
- Model saved for reuse with `joblib`

## 👨‍💻 Author

**Sandeep Patil**  
*M.Tech in AI & ML | Automotive Software | Computer Vision | AUTOSAR*
