# 🚗 Car Resale Price Prediction using ElasticNet

This project demonstrates how to build a machine learning model to predict used car resale prices using **ElasticNet Regression**. The model is trained on a dataset containing car features and their respective resale prices, and it uses a pipeline with proper preprocessing (scaling + encoding) and regularization tuning with `ElasticNetCV`.

## 📁 Files Included

- `car data.csv` – Dataset containing used car features and prices.
- `elasticnet_cv_model.pkl` – Trained ElasticNet model pipeline.
- `README.md` – Project overview and instructions.
- `requirements.txt` – Required Python packages.

## 🧪 Model Summary

- **Model Type**: ElasticNetCV (L1 + L2 regularization)
- **Best Alpha**: Automatically selected
- **Best L1 Ratio**: Automatically selected
- **R² Score**: ~0.84
- **MSE**: ~3.69
- **Preprocessing**: StandardScaler for numericals, OneHotEncoder for categoricals

## 🛠 How to Run

```bash
# Step 1: Clone the repo
git clone https://github.com/yourusername/car-resale-elasticnet.git
cd car-resale-elasticnet

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the notebook (optional) or load the saved model
```

## 🧠 Features Used

- Present Price
- Kms Driven
- Owner Count
- Car Age (Derived from Year)
- Fuel Type, Seller Type, Transmission (Encoded)

## 📈 Libraries Used

- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- joblib

## 💡 Project Highlights

- End-to-end pipeline using `Pipeline` and `ColumnTransformer`
- ElasticNetCV for tuning `alpha` and `l1_ratio`
- Visualization of model performance
- Saved trained model for reuse/deployment

## 👨‍💻 Author

**Sandeep Patil**  
*M.Tech in AI & ML | Automotive Software | Computer Vision*
