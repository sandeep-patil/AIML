from data_preprocessing import preprocess_data
from model import train_logistic_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

def main():
    # Step 1: Load and preprocess the data
    X, y = preprocess_data("data/heart.csv")

    # Step 2: Split into train and test sets (80/20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Step 3: Train logistic regression model
    model = train_logistic_model(X_train, y_train)

    # Step 4: Evaluate on test set
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc = roc_auc_score(y_test, y_pred)

    print("\n Test Set Performance:")
    print(f"Accuracy:  {acc:.4f}")
    print(f"F1 Score:  {f1:.4f}")
    print(f"ROC AUC:   {roc:.4f}")

if __name__ == "__main__":
    main()
