import streamlit as st
import numpy as np
import pickle

modnr = pickle.load(open('moln.pkl', 'rb'))# Loading the pickle files/models.
modpr = pickle.load(open('molp.pkl', 'rb'))
modkr = pickle.load(open('molk.pkl', 'rb'))

# creating adictionary with crop names and soil names corresponding numbers
crop_dict = {
    'rice': 20,
    'maize':11,
    'chickpea':3,
    'kidneybeans':9,
    'pigeonpeas':18,
    'mothbeans':13,
    'mungbean':14,
    'blackgram':2,
    'lentil':10,
    'pomegranate':19,
    'banana':1,
    'mango':12,
    'grapes':7,
    'watermelon':21,
    'muskmelon':15,
    'apple':0,
    'orange':16,
    'papaya':17,
    'coconut':4,
    'cotton':6,
    'jute': 8,
    'coffee':5,
    
}
soil_dict = {
    'Clayey': 0,
    'loamy': 3,
    'red': 4,
    'sandy': 5,
    'sandy loam': 6,
    'alluvial': 1,
    'laterite': 2,
}

# def set_background():
#     st.markdown(
#         """
#         <style>
#         body {
#             background-image: url("D:\\sig\\files\\project\\ferti\\assets\\agri.jpg");
#             background-size: cover;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
agri="""
<style>
[data-testid="stAppViewContainer"]{
    background-image:url("https://img.freepik.com/free-photo/sunny-meadow-landscape_1112-307.jpg?w=1060&t=st=1687845621~exp=1687846221~hmac=8ce1b8ce19b604dd7a1063629e7f07134e1420a9cb3dd0f20c55532834070181");
    background-size: cover;
}
</style>
"""

# Call the markdown() function
st.markdown(agri,unsafe_allow_html=True)

# Create the Streamlit web interface
st.title("Recommender System for Fertilizers")
st.write('Enter the crop name and area to predict NPK values')

# Input form for user to enter crop name and area
crop_name = st.selectbox('Select Crop Name', list(crop_dict.keys()))
soil_name=st.selectbox('Select soil type', list(soil_dict.keys()))
moisture = st.number_input('Enter Moisture')
temperature = st.number_input('Enter Temperature')
humidity = st.number_input('Enter Humidity')
ph = st.number_input('Enter ph')
rainfall = st.number_input('Enter Rainfall')

# Perform predictions when user clicks on the "Predict" button
if st.button('Predict'):
    # Get the crop number corresponding to the selected crop name
    crop_number = crop_dict[crop_name]
    
    # Get the soil number corresponding to the selected soil name
    soil_number = soil_dict[soil_name]
    
    # Reshape the input to match the models' expectations
    value = np.array([[temperature, humidity, ph, rainfall, moisture, crop_number, soil_number]])
    
    # Define the function to get the output for all 3 values together
    def predict_npk(value):
        prediction_N = modnr.predict(value)
        prediction_P = modpr.predict(value)
        prediction_K = modkr.predict(value)
        return prediction_N, prediction_P, prediction_K
    
    # Make the prediction
    prediction_N, prediction_P, prediction_K = predict_npk(value)
    
    # Display the predictions
    st.write('Predicted N:', prediction_N[0])
    st.write('Predicted P:', prediction_P[0])
    st.write('Predicted K:', prediction_K[0])
