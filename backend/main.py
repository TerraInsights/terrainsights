from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
import pandas as pd
import joblib
import os

from database import SessionLocal, engine, Base
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ml', 'fertilizer_model.pkl')
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    print(f"Warning: Model not loaded. {e}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class PredictionInput(BaseModel):
    Soil_Type: str
    Soil_pH: float
    Soil_Moisture: float
    Organic_Carbon: float
    Electrical_Conductivity: float
    Nitrogen_Level: int
    Phosphorus_Level: int
    Potassium_Level: int
    Temperature: float
    Humidity: float
    Rainfall: float
    Crop_Type: str
    Crop_Growth_Stage: str
    Season: str
    Irrigation_Type: str
    Previous_Crop: str
    Region: str
    Fertilizer_Used_Last_Season: float
    Yield_Last_Season: float

@app.get("/")
def read_root():
    return {"message": "Welcome to Fertilizer Optimizer API"}

@app.post("/predict")
def predict_fertilizer(input_data: PredictionInput, db: Session = Depends(get_db)):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    input_dict = input_data.model_dump()
    input_df = pd.DataFrame([input_dict])
    
    prediction = model.predict(input_df)[0]
    
    db_history = models.PredictionHistory(
        soil_type=input_data.Soil_Type,
        soil_ph=input_data.Soil_pH,
        crop_type=input_data.Crop_Type,
        season=input_data.Season,
        recommended_fertilizer=prediction
    )
    db.add(db_history)
    db.commit()
    
    return {"recommended_fertilizer": prediction}

@app.get("/history")
def get_history(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    history = db.query(models.PredictionHistory).offset(skip).limit(limit).all()
    return history
