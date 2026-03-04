import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("Hypertension Risk Prediction")

gender = st.number_input("Gender code")
smoking = st.number_input("Smoking code")
alcohol = st.number_input("Alcohol code")
stress = st.number_input("Stress score")
physical = st.number_input("Physical activity code")
salt = st.number_input("Salt intake code")
glucose = st.number_input("Glucose")
bmi = st.number_input("BMI")
age = st.number_input("Age")

if st.button("Predict"):
    data = np.array([[gender, smoking, alcohol, stress,
                      physical, salt, glucose, bmi, age]])
    
    prediction = model.predict(data)
    
    if prediction[0] == 1:
        st.error("High risk of hypertension")
    else:
        st.success("Low risk of hypertension")
