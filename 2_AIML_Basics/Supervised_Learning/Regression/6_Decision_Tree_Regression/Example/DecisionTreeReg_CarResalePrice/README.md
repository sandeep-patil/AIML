# 🚗 Car Resale Price Prediction using Decision Tree Regression

This project builds a Decision Tree Regression model to predict car resale prices using the CarDekho dataset. The model is interpretable and well-suited for mixed feature types (categorical + numerical) without requiring feature scaling.

## 📁 Files Included

- `car data.csv` – Dataset used for training
- `DecisionTreeReg_CarResalePrice.ipynb` – Complete notebook with step-by-step model development
- `DecisionTreeReg_CarResalePrice.pkl` – Trained Decision Tree Regression model
- `README.md` – This file
- `requirements.txt` – Required Python packages

## 🔧 Model Summary

- **Model**: Decision Tree Regressor
- **Max Depth**: 4
- **Feature Selection**: Automatic through best-split selection
- **Handles Non-Linearity**: ✅ Yes
- **Handles Categorical Features**: ✅ Yes (via one-hot encoding)
- **No Feature Scaling Required**: ✅
- **Final R² Score**: ~0.87–0.92 (depending on depth)
- **Final MSE**: Low (on test set)

## 🛠 How to Run

```bash
# Step 1: Clone the repo
git clone https://github.com/yourusername/car-resale-decisiontree.git
cd car-resale-decisiontree

# Step 2: Install requirements
pip install -r requirements.txt

# Step 3: Run the notebook or load the model
```

## 🧠 Features Used

- Present_Price
- Kms_Driven
- Owner
- Car_Age
- Fuel_Type, Seller_Type, Transmission (one-hot encoded)

## 🧩 Advantages of Decision Tree

- No need for scaling
- Works with both numerical and categorical data
- Highly interpretable (view model as a flowchart)
- Handles non-linear relationships automatically

## 👨‍💻 Author

**Sandeep Patil**  
*M.Tech in AI & ML | Automotive Software | Computer Vision*
