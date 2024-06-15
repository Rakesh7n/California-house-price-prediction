import streamlit as st
import pickle
import numpy as np
# Load the model
model = pickle.load(open('GBRmodel.pkl', 'rb'))
st.title("California House Price Prediction")
# Create input fields for the user
longitude = st.number_input("Longitude")
latitude = st.number_input("Latitude")
housing_median_age = st.number_input("Housing Median Age")
total_rooms = st.number_input("Total Rooms")
total_bedrooms = st.number_input("Total Bedrooms")
population = st.number_input("Population")
households = st.number_input("Households")
median_income = st.number_input("Median Income")
ocean_proximity_OCEAN=st.number_input("ocean_proximity_OCEAN")
ocean_proximity_INLAND=st.number_input("ocean_proximity_INLAND")
ocean_proximity_ISLAND=st.number_input("ocean_proximity_ISLAND")
ocean_proximity_NEARBAY=st.number_input("ocean_proximity_NEARBAY")
ocean_proximity_NEAROCEAN=st.number_input("ocean_proximity_NEAROCEAN")
   
def predict_house_price():
    # Convert input values to a numpy array
    input_values = np.array([
        longitude,
        latitude,
        housing_median_age,
        total_rooms,
        total_bedrooms,
        population,
        households,
        median_income,
        ocean_proximity_OCEAN,
        ocean_proximity_INLAND,
        ocean_proximity_ISLAND,
        ocean_proximity_NEARBAY,
        ocean_proximity_NEAROCEAN
          ])
    
    result = model.predict(input_values.reshape(1, -1))[0]
    # Format the result
    output = "${:.2f}".format(result)
    return output

# Create a button to trigger the prediction
if st.button("Predict"):
    result = predict_house_price()
    st.write("Predicted House Price: ", result)