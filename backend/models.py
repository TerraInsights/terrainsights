from sqlalchemy import Column, Integer, String, Float
from database import Base

class PredictionHistory(Base):
    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True, index=True)
    soil_type = Column(String)
    soil_ph = Column(Float)
    crop_type = Column(String)
    season = Column(String)
    recommended_fertilizer = Column(String)
