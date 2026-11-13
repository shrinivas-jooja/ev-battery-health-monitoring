
import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# 1. Load dataset
DATA_PATH = Path("datasets/ev_battery_4cell_synthetic_dataset_fixed.csv")

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# 2. Select input features
features = [
    "cell_1_voltage_V",
    "cell_2_voltage_V",
    "cell_3_voltage_V",
    "cell_4_voltage_V",
    "pack_voltage_V",
    "current_A",
    "temperature_C",
    "SoC_percent",
    "voltage_delta_V"
]

X = df[features]
y = df["label"]

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# 4. Create Random Forest model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=12,
    random_state=42,
    class_weight="balanced"
)

# 5. Train model
model.fit(X_train, y_train)

print("\nModel training completed!")

# 6. Make predictions
y_pred = model.predict(X_test)

# 7. Evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 8. Save trained model and feature names
Path("models").mkdir(exist_ok=True)

joblib.dump(
    {"model": model, "features": features},
    "models/battery_safety_model.pkl"
)

print("\nModel saved successfully!")
print("Location: models/battery_safety_model.pkl")
