from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
from utils import save_model
from utils import get_logger
logger = get_logger()

def train_random_forest_model(X_train, y_train):
    logger.info(" Entered train_random_forest_model()")
    # === 3. Define final model pipeline with best parameters ===
    model = make_pipeline(
        StandardScaler(),
        RandomForestClassifier(
            n_estimators=180,
            max_depth=15,
            min_samples_split=9,
            min_samples_leaf=4,
            bootstrap=True,
            random_state=42
        )
    )

    # === 4. Cross-validation on training set ===
    cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='f1')
    logger.info(f"Cross-validated F1 Scores: {cv_scores}")
    logger.info(f"🔁 Mean F1 Score (CV): {cv_scores.mean():.4f}")

    # === 5. Train final model ===
    model.fit(X_train, y_train)

    save_model(model, "../model.pkl")

    return model
