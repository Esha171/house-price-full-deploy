from fastapi import FastAPI
from pydantic import BaseModel
import cloudpickle
import numpy as np
import os

app = FastAPI()

# ✅ Load best model using cloudpickle
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "best_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = cloudpickle.load(f)

# --- Pydantic schema for input data ---
class HouseFeatures(BaseModel):
    area: int
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: int
    guestroom: int
    basement: int
    hotwaterheating: int
    airconditioning: int
    parking: int
    prefarea: int
    furnishingstatus: int

# --- Routes ---
@app.get("/")
def read_root():
    return {"message": "Welcome to the House Price Prediction API 🏠"}

@app.get("/health")
def health_check():
    return {"status": "API is running 🚀"}

@app.post("/predict")
def predict_price(data: HouseFeatures):
    features = np.array([[data.area, data.bedrooms, data.bathrooms, data.stories,
                          data.mainroad, data.guestroom, data.basement, data.hotwaterheating,
                          data.airconditioning, data.parking, data.prefarea, data.furnishingstatus]])
    
    prediction = model.predict(features)
    return {"predicted_price": float(prediction[0])}
