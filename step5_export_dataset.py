
import pandas as pd
from pathlib import Path

# Load the generated 4-cell dataset
input_file = "datasets/ev_battery_4cell_synthetic_dataset.csv"

df = pd.read_csv(input_file)

# Create Excel output
output_file = Path("datasets/ev_battery_4cell_records.xlsx")

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    # All 3000 records
    df.to_excel(
        writer,
        sheet_name="All Battery Records",
        index=False
    )

    # Summary of safety classes
    df["label"].value_counts().rename_axis(
        "Safety Status"
    ).reset_index(name="Record Count").to_excel(
        writer,
        sheet_name="Class Distribution",
        index=False
    )

    # First 100 records for quick viewing
    df.head(100).to_excel(
        writer,
        sheet_name="First 100 Records",
        index=False
    )

print("Excel file created successfully!")
print("Total records:", len(df))
print("Saved at:", output_file)
