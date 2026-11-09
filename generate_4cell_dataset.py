
import numpy as np
import pandas as pd
from pathlib import Path

# ==========================================================
# 1. CONFIGURATION
# ==========================================================

np.random.seed(42)

NUMBER_OF_SAMPLES = 3000

OUTPUT_FOLDER = Path("datasets")
OUTPUT_FOLDER.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_FOLDER / "ev_battery_4cell_synthetic_dataset_fixed.csv"

records = []

# ==========================================================
# 2. GENERATE SYNTHETIC BATTERY DATA
# ==========================================================

for i in range(NUMBER_OF_SAMPLES):

    # Intended operating scenario
    condition = np.random.choice(
        ["NORMAL", "WARNING", "CRITICAL"],
        p=[0.60, 0.25, 0.15]
    )

    # Battery State of Charge
    soc = np.random.uniform(10, 100)

    # Approximate cell voltage model for simulation
    base_voltage = 3.0 + (soc / 100) * 1.15

    # Generate four cell voltages
    cells = np.random.normal(
        base_voltage,
        0.008,
        4
    )

    # ------------------------------------------------------
    # 3. SIMULATE OPERATING CONDITIONS
    # ------------------------------------------------------

    if condition == "NORMAL":

        temperature = np.random.uniform(20, 40)
        current = np.random.uniform(-20, 20)

    elif condition == "WARNING":

        # Moderate voltage imbalance
        fault_cell = np.random.randint(0, 4)

        cells[fault_cell] -= np.random.uniform(
            0.09, 0.13
        )

        temperature = np.random.uniform(45, 54.9)
        current = np.random.uniform(-35, 35)

    else:

        # Severe voltage imbalance
        fault_cell = np.random.randint(0, 4)

        cells[fault_cell] -= np.random.uniform(
            0.18, 0.35
        )

        temperature = np.random.uniform(55, 70)
        current = np.random.uniform(-50, 50)

    # ------------------------------------------------------
    # 4. CELL VOLTAGE LIMITING
    # ------------------------------------------------------

    # Clip before performing any calculations
    cells = np.clip(cells, 2.5, 4.2)

    # Round individual cell voltages
    cells = np.round(cells, 3)

    c1, c2, c3, c4 = cells

    rounded_cells = [c1, c2, c3, c4]

    # Round other measurements
    rounded_soc = round(soc, 2)
    rounded_temp = round(temperature, 1)
    rounded_current = round(current, 2)

    # ------------------------------------------------------
    # 5. CALCULATE BATTERY PARAMETERS
    # ------------------------------------------------------

    # Four-cell series pack voltage
    pack_voltage = round(
        sum(rounded_cells), 3
    )

    # Cell voltage imbalance
    voltage_delta = round(
        max(rounded_cells) - min(rounded_cells),
        3
    )

    # Minimum cell voltage
    minimum_cell_voltage = min(rounded_cells)

    # ------------------------------------------------------
    # 6. SAFETY CLASSIFICATION
    # ------------------------------------------------------

    if (
        voltage_delta >= 0.15
        or rounded_temp >= 55.0
        or minimum_cell_voltage <= 2.8
    ):

        safety_status = "CRITICAL"

    elif (
        voltage_delta >= 0.08
        or rounded_temp >= 45.0
        or minimum_cell_voltage <= 3.0
    ):

        safety_status = "WARNING"

    else:

        safety_status = "NORMAL"

    # ------------------------------------------------------
    # 7. STORE RECORD
    # ------------------------------------------------------

    records.append({

        "sample_id": i + 1,

        # Intended scenario, not the final AI target
        "operating_condition": condition,

        "cell_1_voltage_V": c1,
        "cell_2_voltage_V": c2,
        "cell_3_voltage_V": c3,
        "cell_4_voltage_V": c4,

        "pack_voltage_V": pack_voltage,

        "current_A": rounded_current,

        "temperature_C": rounded_temp,

        "SoC_percent": rounded_soc,

        "voltage_delta_V": voltage_delta,

        # Final rule-based classification target
        "label": safety_status
    })


# ==========================================================
# 8. CREATE DATAFRAME
# ==========================================================

df = pd.DataFrame(records)


# ==========================================================
# 9. DATA QUALITY VALIDATION
# ==========================================================

cell_columns = [
    "cell_1_voltage_V",
    "cell_2_voltage_V",
    "cell_3_voltage_V",
    "cell_4_voltage_V"
]

calculated_pack = df[cell_columns].sum(axis=1).round(3)

calculated_delta = (
    df[cell_columns].max(axis=1)
    - df[cell_columns].min(axis=1)
).round(3)

pack_mismatches = (
    calculated_pack != df["pack_voltage_V"]
).sum()

delta_mismatches = (
    calculated_delta != df["voltage_delta_V"]
).sum()

voltage_violations = (
    (df[cell_columns] < 2.5)
    | (df[cell_columns] > 4.2)
).sum().sum()

missing_values = df.isnull().sum().sum()

duplicate_records = df.duplicated().sum()

condition_label_differences = (
    df["operating_condition"] != df["label"]
).sum()


# ==========================================================
# 10. SAVE DATASET
# ==========================================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)


# ==========================================================
# 11. DISPLAY RESULTS
# ==========================================================

print("\n" + "=" * 60)

print("4-CELL EV BATTERY DATASET GENERATED SUCCESSFULLY")

print("=" * 60)

print("\nDATASET INFORMATION")

print("Total samples:", len(df))
print("Total columns:", len(df.columns))

print("\nCLASS DISTRIBUTION")

print(df["label"].value_counts())

print("\nCLASS DISTRIBUTION PERCENTAGE")

print(
    (df["label"].value_counts(normalize=True) * 100)
    .round(2)
)

print("\nDATA QUALITY VALIDATION")

print("Cell voltage violations:", voltage_violations)
print("Pack voltage mismatches:", pack_mismatches)
print("Voltage delta mismatches:", delta_mismatches)
print("Missing values:", missing_values)
print("Duplicate records:", duplicate_records)

print(
    "Condition-label differences:",
    condition_label_differences
)

print("\nCELL VOLTAGE RANGES")

print(
    df[cell_columns].agg(["min", "max", "mean"])
)

print("\nFIRST FIVE RECORDS")

print(df.head())

print("\nDATASET SAVED AT:")

print(OUTPUT_FILE)

print("\n" + "=" * 60)
print("DATA GENERATION COMPLETED")
print("=" * 60)
