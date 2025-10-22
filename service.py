from fastapi import FastAPI
from pydantic import BaseModel


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
    ocean_oneH_OCEAN: bool
    ocean_INLAND: bool
    ocean_ISLAND: bool
    ocean_NEAR_BAY: bool
    ocean_NEAR_OCEAN: bool

app = FastAPI()


@app.post('/score')
def score(data: HouseData):
    price = data.total_rooms > 2.0
    return {'price': price}


