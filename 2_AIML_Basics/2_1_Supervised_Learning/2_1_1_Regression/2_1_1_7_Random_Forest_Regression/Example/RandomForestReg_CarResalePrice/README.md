# 🚗 Car Resale Price Prediction using Random Forest Regression

This project demonstrates a machine learning pipeline using **Random Forest Regression** to predict the selling price of used cars. It is built on the CarDekho dataset and captures both linear and non-linear relationships between features and price.

## 📁 Files Included

- `car data.csv` – Dataset used for training
- `RandomForestReg_CarResalePrice.ipynb` – Full model development notebook
- `RandomForestReg_CarResalePrice.pkl` – Saved trained Random Forest model
- `README.md` – Project overview and usage instructions
- `requirements.txt` – List of required Python libraries

## 🧠 Model Summary

- **Model Type**: Random Forest Regressor
- **n_estimators**: 100
- **max_depth**: 6
- **Handles Non-Linearity**: ✅
- **Feature Scaling Needed**: ❌ No
- **Feature Importance Available**: ✅ Yes
- **R² Score**: ~0.958
- **MSE**: ~0.97

## 🛠 How to Run

```bash
# Step 1: Clone the repository
git clone https://github.com/yourusername/car-resale-rf.git
cd car-resale-rf

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the notebook or load the saved model
```

## 🔍 Features Used

- Present_Price
- Kms_Driven
- Owner
- Car_Age (derived from Year)
- Fuel_Type, Seller_Type, Transmission (one-hot encoded)

## 💡 Key Advantages of Random Forest

- Handles complex feature interactions
- Less prone to overfitting than a single decision tree
- Provides automatic feature selection via importance
- Works well even without feature scaling

## 📜 License

MIT License

## 👨‍💻 Author

**Sandeep Patil**  
*M.Tech in AI & ML | Automotive Software | Computer Vision | AUTOSAR*
