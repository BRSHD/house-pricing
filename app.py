import streamlit as st
import pandas as pd
import joblib
import numpy as np
import requests

model = joblib.load('GB_model.pkl')

st.title("California House Price Prediction")

longitude = st.number_input("Longitude", value=-118.49)
latitude = st.number_input("Latitude", value=34.01)
housing_median_age = st.number_input("Housing Median Age", value=28.0)
total_rooms = st.number_input("Total Rooms", value=2100.0)
total_bedrooms = st.number_input("Total Bedrooms", value=420.0)
population = st.number_input("Population", value=1200.0)
households = st.number_input("Households", value=400.0)
median_income = st.number_input("Median Income", value=4.5)
rooms_per_household = st.number_input("Rooms per Household", value=5.25)
bedrooms_per_room = st.number_input("Bedrooms per Room", value=0.2)
population_per_household = st.number_input("Population per Household", value=3.0)
income_per_person = st.number_input("Income per Person", value=1.5)


st.write("Ocean Proximity:")
H_OCEAN = st.checkbox("<1H_OCEAN")
INLAND = st.checkbox("INLAND")
ISLAND = st.checkbox("ISLAND")
NEAR_BAY = st.checkbox("NEAR_BAY")
NEAR_OCEAN = st.checkbox("NEAR_OCEAN")

if st.button("Predict Price"):
    try:
        
        features = {
            'longitude': longitude,
            'latitude': latitude,
            'housing_median_age': housing_median_age,
            'total_rooms': total_rooms,
            'total_bedrooms': total_bedrooms,
            'population': population,
            'households': households,
            'median_income': median_income,
            'rooms_per_household': rooms_per_household,
            'bedrooms_per_room': bedrooms_per_room,
            'population_per_household': population_per_household,
            'income_per_person': income_per_person,
            'H_OCEAN': H_OCEAN,
            'INLAND': INLAND,
            'ISLAND': ISLAND,
            'NEAR_BAY': NEAR_BAY,
            'NEAR_OCEAN': NEAR_OCEAN
        }
        
        response = requests.post('http://127.0.0.1:8000/score', json = features)
        st.success(response.json())
        
    except Exception as e:
        st.error(f"Error: {str(e)}")