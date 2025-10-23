from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd


class HouseData(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float
    rooms_per_household: float
    bedrooms_per_room: float
    population_per_household: float
    income_per_person: float
    H_OCEAN: bool
    INLAND: bool
    ISLAND: bool
    NEAR_BAY: bool
    NEAR_OCEAN: bool

app = FastAPI()
model = joblib.load('GB_model.pkl')

@app.post('/score')
def score(data: HouseData):
    features_list = [
        data.longitude, data.latitude, data.housing_median_age, data.total_rooms,
        data.total_bedrooms, data.population, data.households, data.median_income,
        data.rooms_per_household, data.bedrooms_per_room, data.population_per_household,
        data.income_per_person, data.H_OCEAN, data.INLAND, data.ISLAND, data.NEAR_BAY,
        data.NEAR_OCEAN
    ]
    
    # Двумерный список: [[features]]
    price = model.predict([features_list])[0]
    price_value = float(price)
    
    return {'price': price_value}
