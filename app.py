import streamlit as st
import pandas as pd
import pickle
import math



# streamlit run app.py 
data = pd.read_csv('Cleaned_data.csv')
house = pickle.load(open('RidgeModel.pkl','rb'))

st.title('Banglore House Price Predictor')

location = st.selectbox(
    'Select Location',
    sorted(data['location'].unique()))

bhk = st.selectbox(
    'Select Number of BHK',
    sorted(data['bhk'].unique()))

bath = st.selectbox(
    'Select Number of Bathrooms',
    sorted(data['bath'].unique()))

sqft = st.text_input(
    'Select Expected Area in SQFT')

input_value= pd.DataFrame([[location,bhk,bath,sqft]], columns=['location','bhk','bath','total_sqft'])

if st.button('Predicted House Value'):
    st.info(f"Predicted Valuation of the house is: ₹ *{math.ceil(house.predict(input_value)[0]*100000)}*")
    