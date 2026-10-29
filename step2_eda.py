
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("ev_battery_synthetic_1000_dataset.csv")

sns.set_theme(style="whitegrid")

# Graph 1: Target class distribution
plt.figure(figsize=(7, 5))
sns.countplot(
    data=df,
    x="label",
    order=["normal", "warning", "critical"]
)
plt.title("Distribution of Battery Condition Labels")
plt.xlabel("Battery Condition")
plt.ylabel("Number of Samples")
plt.tight_layout()
plt.savefig("eda_label_distribution.png", dpi=150)
plt.show()

# Graph 2: Pack voltage by battery condition
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="label",
    y="pack_voltage_V",
    order=["normal", "warning", "critical"]
)
plt.title("Pack Voltage by Battery Condition")
plt.xlabel("Battery Condition")
plt.ylabel("Pack Voltage (V)")
plt.tight_layout()
plt.savefig("eda_pack_voltage.png", dpi=150)
plt.show()

# Graph 3: State of Charge by battery condition
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="label",
    y="SoC_percent",
    order=["normal", "warning", "critical"]
)
plt.title("State of Charge by Battery Condition")
plt.xlabel("Battery Condition")
plt.ylabel("State of Charge (%)")
plt.tight_layout()
plt.savefig("eda_soc.png", dpi=150)
plt.show()

# Graph 4: Individual cell voltage distributions
cell_cols = [
    f"cell_{i}_voltage_V" for i in range(1, 13)
]

plt.figure(figsize=(12, 6))
sns.boxplot(data=df[cell_cols])
plt.title("Voltage Distribution Across 12 Battery Cells")
plt.xlabel("Battery Cell")
plt.ylabel("Cell Voltage (V)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("eda_cell_voltages.png", dpi=150)
plt.show()

print("EDA completed. Four graphs have been saved.")
