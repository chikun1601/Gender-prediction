# app.py
import streamlit as st
import pickle
import numpy as np

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Title and description
st.markdown("<h1 style='color: blue;'>Gender Prediction App</h1>", unsafe_allow_html=True)

st.write("This app predicts gender based on height and weight.")

# Input fields
height = st.number_input("Enter height (cm)", min_value=50, max_value=800, step=1)
weight = st.number_input("Enter weight (kg)", min_value=60, max_value=300, step=1)

# Predict button
if st.button("Predict Gender"):
    # Prepare input data
    input_data = np.array([[height, weight]])
    # Make prediction
    prediction = model.predict(input_data)[0]
    gender = "Male" if prediction == 1 else "Female"
    # Display result
    st.write(f"The predicted gender is: **{gender}**")
