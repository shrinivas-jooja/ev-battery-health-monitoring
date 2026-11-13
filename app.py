
import joblib

from fastapi import FastAPI
from pydantic import BaseModel

# Initialize API
app = FastAPI(title="EV Battery Monitoring API")

# Load trained model
saved_data = joblib.load("models/battery_safety_model.pkl")

model = saved_data["model"]
features = saved_data["features"]


# Battery input structure
class BatteryData(BaseModel):
    cell_1_voltage_V: float
    cell_2_voltage_V: float
    cell_3_voltage_V: float
    cell_4_voltage_V: float
    pack_voltage_V: float
    current_A: float
    temperature_C: float
    SoC_percent: float
    voltage_delta_V: float


@app.get("/")
def home():
    return {"message": "EV Battery Monitoring API is running"}


@app.post("/predict")
def predict_battery(data: BatteryData):

    input_data = data.model_dump()

    import pandas as pd
    input_df = pd.DataFrame([input_data])[features]

    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]

    return {
        "predicted_status": prediction,
        "probabilities": {
            label: round(float(prob) * 100, 2)
            for label, prob in zip(model.classes_, probabilities)
        }
    }
