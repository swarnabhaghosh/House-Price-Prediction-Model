import streamlit as st
import pickle
import numpy as np

# Load the trained pipeline model
with open("price_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

# Title
st.title("🏠 House Price Prediction App")
st.write("Enter the details below to predict the house price.")

# Input fields
gr_liv_area = st.number_input("Above Ground Living Area (GrLivArea)", min_value=0)
bedroom_abv_gr = st.number_input("Number of Bedrooms Above Ground (BedroomAbvGr)", min_value=0)
full_bath = st.number_input("Number of Full Bathrooms (FullBath)", min_value=0)

# Predict button
if st.button("Predict"):
    # Create input array
    input_data = np.array([[gr_liv_area, bedroom_abv_gr, full_bath]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Output result
    st.success(f"🏷️ Estimated House Price: ${prediction[0]:,.2f}")
