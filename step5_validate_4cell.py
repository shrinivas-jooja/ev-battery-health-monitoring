
import pandas as pd

# 1. Load the new 4-cell dataset
file_path = "datasets/ev_battery_4cell_synthetic_dataset.csv"
df = pd.read_csv(file_path)

print("=" * 50)
print("EV BATTERY 4-CELL DATASET INSPECTION")
print("=" * 50)

# 2. Dataset dimensions
print("\n1. DATASET SHAPE")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 3. Display column names
print("\n2. COLUMN NAMES")
print(df.columns.tolist())

# 4. Display first five records
print("\n3. FIRST FIVE RECORDS")
print(df.head())

# 5. Check data types
print("\n4. DATA TYPES")
print(df.dtypes)

# 6. Check missing values
print("\n5. MISSING VALUES")
print(df.isnull().sum())

# 7. Check duplicate records
print("\n6. DUPLICATE RECORDS")
print(df.duplicated().sum())

# 8. Safety class distribution
print("\n7. SAFETY CLASS DISTRIBUTION")
print(df["label"].value_counts())

# 9. Statistical summary
print("\n8. STATISTICAL SUMMARY")
print(df.describe())

# 10. Check cell voltage ranges
cell_columns = [
    "cell_1_voltage_V",
    "cell_2_voltage_V",
    "cell_3_voltage_V",
    "cell_4_voltage_V"
]

print("\n9. CELL VOLTAGE RANGES")
print(df[cell_columns].agg(["min", "max", "mean"]))

print("\nDATASET INSPECTION COMPLETED!")
