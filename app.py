
import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

st.title("Student Performance Prediction")

# User Input
math_score = st.number_input("Math Score", min_value=0, max_value=100, value=70)
reading_score = st.number_input("Reading Score", min_value=0, max_value=100, value=70)

# Predict Writing Score
if st.button("Predict Writing Score"):
    input_data = np.array([[math_score, reading_score]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Writing Score: {prediction[0]:,.2f}")
    