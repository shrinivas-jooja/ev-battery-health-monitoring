
import numpy as np
import pandas as pd
from pathlib import Path

# Reproducible synthetic dataset
np.random.seed(42)

NUMBER_OF_SAMPLES = 3000
records = []

for i in range(NUMBER_OF_SAMPLES):

    # Generate three operating conditions
    condition = np.random.choice(
        ["NORMAL", "WARNING", "CRITICAL"],
        p=[0.60, 0.25, 0.15]
    )

    # Simulated battery operating values
    soc = np.random.uniform(10, 100)

    # Approximate cell voltage for demonstration.
    # Replace these assumptions with actual battery data.
    base_voltage = 3.0 + (soc / 100) * 1.15

    cells = np.random.normal(base_voltage, 0.008, 4)

    if condition == "NORMAL":
        temperature = np.random.uniform(20, 40)
        current = np.random.uniform(-20, 20)

    elif condition == "WARNING":
        cells[np.random.randint(0, 4)] -= np.random.uniform(0.08, 0.14)
        temperature = np.random.uniform(45, 55)
        current = np.random.uniform(-35, 35)

    else:
        cells[np.random.randint(0, 4)] -= np.random.uniform(0.16, 0.28)
        temperature = np.random.uniform(56, 70)
        current = np.random.uniform(-50, 50)

    cells = np.clip(cells, 2.8, 4.2)

    # Four-cell series pack voltage
    pack_voltage = np.sum(cells)

    # Cell voltage imbalance
    voltage_delta = np.max(cells) - np.min(cells)

    # Safety status
    # These are provisional synthetic lab thresholds,
    # NOT official thresholds from the project PDF.
    if voltage_delta >= 0.15 or temperature >= 55:
        safety_status = "CRITICAL"

    elif voltage_delta >= 0.08 or temperature >= 45:
        safety_status = "WARNING"

    else:
        safety_status = "NORMAL"

    records.append({
        "sample_id": i + 1,
        "operating_condition": condition,
        "cell_1_voltage_V": round(cells[0], 3),
        "cell_2_voltage_V": round(cells[1], 3),
        "cell_3_voltage_V": round(cells[2], 3),
        "cell_4_voltage_V": round(cells[3], 3),
        "pack_voltage_V": round(pack_voltage, 3),
        "current_A": round(current, 2),
        "temperature_C": round(temperature, 1),
        "SoC_percent": round(soc, 2),
        "voltage_delta_V": round(voltage_delta, 3),
        "label": safety_status
    })

# Create DataFrame
df = pd.DataFrame(records)

# Save dataset
output_folder = Path("datasets")
output_folder.mkdir(exist_ok=True)

output_file = output_folder / "ev_battery_4cell_synthetic_dataset.csv"

df.to_csv(output_file, index=False)

print("4-cell EV battery dataset generated successfully!")
print("Dataset shape:", df.shape)

print("\nClass distribution:")
print(df["label"].value_counts())

print("\nDataset columns:")
print(df.columns.tolist())

print("\nFirst five records:")
print(df.head())

print("\nSaved at:", output_file)
