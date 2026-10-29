
import pandas as pd

df = pd.read_csv("ev_battery_synthetic_1000_dataset.csv")

print("\n===== LABEL vs ABNORMALITY TYPE =====")
print(pd.crosstab(
    df["abnormality_type"],
    df["label"],
    margins=True
))

print("\n===== OPERATING CONDITION vs LABEL =====")
print(pd.crosstab(
    df["operating_condition"],
    df["label"],
    margins=True
))

print("\n===== PACK VOLTAGE BY LABEL =====")
print(df.groupby("label")["pack_voltage_V"].agg(
    ["count", "mean", "std", "min", "max"]
).round(3))

print("\n===== CURRENT BY LABEL =====")
print(df.groupby("label")["current_A"].agg(
    ["count", "mean", "std", "min", "max"]
).round(3))

print("\n===== SOC BY LABEL =====")
print(df.groupby("label")["SoC_percent"].agg(
    ["count", "mean", "std", "min", "max"]
).round(3))

print("\n===== LABEL CHECK COMPLETE =====")
