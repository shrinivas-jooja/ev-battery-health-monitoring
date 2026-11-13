
import pandas as pd
import joblib

# Load saved model
saved_data = joblib.load("models/battery_safety_model.pkl")

model = saved_data["model"]
features = saved_data["features"]

# Load dataset
df = pd.read_csv(
    "datasets/ev_battery_4cell_synthetic_dataset_fixed.csv"
)

# Select one sample
sample = df[features].iloc[[0]]
actual_label = df["label"].iloc[0]

# Predict battery condition
prediction = model.predict(sample)[0]
probabilities = model.predict_proba(sample)[0]

print("Actual Status:", actual_label)
print("Predicted Status:", prediction)

print("\nPrediction Probabilities:")

for label, probability in zip(
    model.classes_, probabilities
):
    print(f"{label}: {probability * 100:.2f}%")
