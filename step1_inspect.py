
import pandas as pd
from pathlib import Path

# Locate the dataset in the current project folder
file_path = Path("ev_battery_synthetic_1000_dataset.csv")

if not file_path.exists():
    print("ERROR: Dataset file not found!")
else:
    df = pd.read_csv(file_path)

    print("\n===== DATASET SHAPE =====")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\n===== COLUMN NAMES =====")
    print(df.columns.tolist())

    print("\n===== FIRST 5 ROWS =====")
    print(df.head())

    print("\n===== DATA TYPES =====")
    print(df.dtypes)

    print("\n===== MISSING VALUES =====")
    print(df.isnull().sum())

    print("\n===== DUPLICATE ROWS =====")
    print(df.duplicated().sum())

    if "label" in df.columns:
        print("\n===== CLASS DISTRIBUTION =====")
        print(df["label"].value_counts())
        print("\n===== CLASS DISTRIBUTION (%) =====")
        print(df["label"].value_counts(normalize=True).mul(100).round(2))

    print("\n===== NUMERICAL SUMMARY =====")
    print(df.describe().T)

    print("\n===== INSPECTION COMPLETE =====")
