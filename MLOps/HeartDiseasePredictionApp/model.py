from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
import joblib

def train_logistic_model(X_train, y_train):
    # Initialize logistic regression model
    model = LogisticRegression(max_iter=2000)

    # Optional: 5-fold cross-validation on training data
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='f1')
    print(f"🔁 Cross-validated F1 scores (training only): {scores}")
    print(f"🔁 Mean Cross-Validated F1 Score: {scores.mean():.4f}")

    # Train the model on full training set
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, 'logistic_model.pkl')
    print("Model saved as 'logistic_model.pkl'")

    return model
