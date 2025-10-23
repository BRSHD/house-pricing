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
    features = pd.DataFrame([{
        'longitude': data.longitude,
        'latitude': data.latitude,
        'housing_median_age': data.housing_median_age,
        'total_rooms': data.total_rooms,
        'total_bedrooms': data.total_bedrooms,
        'population': data.population,
        'households': data.households,
        'median_income': data.median_income,
        'rooms_per_household': data.rooms_per_household,
        'bedrooms_per_room': data.bedrooms_per_room,
        'population_per_household': data.population_per_household,
        'income_per_person': data.income_per_person,
        'ocean_proximity_H_OCEAN': data.H_OCEAN,
        'ocean_proximity_INLAND': data.INLAND,
        'ocean_proximity_ISLAND': data.ISLAND,
        'ocean_proximity_NEAR_BAY': data.NEAR_BAY,
        'ocean_proximity_NEAR_OCEAN': data.NEAR_OCEAN
    }])

    price = model.predict([features])[0]

    return {'price': price}

