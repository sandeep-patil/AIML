from data_preprocessing import preprocess_data
from model import train_random_forest_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix
)
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from utils import get_logger

logger = get_logger()

def main():
    # Step 1: Load and preprocess the data
    X, y = preprocess_data("../data/processed_cleveland_data.csv")

    # Step 2: Split into train and test sets (80/20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Step 3: Train Random Forest model
    model = train_random_forest_model(X_train, y_train)

    # Step 4: Evaluate on test set
    y_pred = model.predict(X_test)

    # Evaluate metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    cm = confusion_matrix(y_test, y_pred)

    # Display results
    logger.info("\n Test Set Performance:")
    logger.info(f"Accuracy:        {acc:.4f}")
    logger.info(f"Precision:       {prec:.4f}")
    logger.info(f"Recall:          {rec:.4f}")
    logger.info(f"F1 Score:        {f1:.4f}")
    logger.info(f"ROC AUC Score:   {roc:.4f}")
    logger.info("Confusion Matrix:")
    logger.info(cm)


    # === ROC Curve ===
    y_proba = model.predict_proba(X_test)[:, 1]  # Get probabilities for class 1
    fpr, tpr, thresholds = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC Curve (AUC = {roc_auc:.4f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()




if __name__ == "__main__":
    main()
