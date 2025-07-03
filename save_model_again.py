# 1. Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import  OneHotEncoder

# 2. Load dataset
df = pd.read_csv("data/predictive_maintenance.csv")  
# Drop unnecessary columns
df.drop(columns=['UDI', 'Product ID'], inplace=True)

# 3. Define features (X) and target (y)
X = df.drop(columns=['Target','Failure Type'] ,axis=1)  
y = df["Target"]

# 4. Detect numeric and categorical columns
numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_features = X.select_dtypes(include=["object", "category"]).columns.tolist()

# 5. Preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# 6. Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# 7. Build the Pipeline
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("smote", SMOTE(random_state=42)),
    ("classifier", XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss'))
])

# 8. Hyperparameter Search Space
param_grid = {
    "classifier__n_estimators": [100, 200],
    "classifier__max_depth": [3, 5, 7],
    "classifier__learning_rate": [0.01, 0.1, 0.3],
    "classifier__subsample": [0.8, 1.0],
    "classifier__colsample_bytree": [0.8, 1.0],
}

# 9. Randomized Search
search = RandomizedSearchCV(
    pipeline,
    param_distributions=param_grid,
    n_iter=10,
    scoring="f1",
    cv=3,
    verbose=2,
    n_jobs=-1,
    random_state=42
)

# 10. Fit
search.fit(X_train, y_train)

# 11. Evaluate
y_pred = search.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

import joblib

# Suppose your model pipeline is named: xgb_pipeline
joblib.dump(search, 'predictive_maintenance_dashboard/model/xgb_pipeline_model.joblib')