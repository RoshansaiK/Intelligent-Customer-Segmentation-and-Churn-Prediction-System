import streamlit as st
import joblib
import numpy as np

st.title("Telco Customer Churn Prediction")

model = joblib.load("churn_model.pkl")

st.write("### Enter Customer Information:")

gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 24)
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0)

binary_map = {"Yes": 1, "No": 0, "Male": 1, "Female": 0}

input_data = np.array([[
    binary_map[gender],
    SeniorCitizen,
    binary_map[Partner],
    binary_map[Dependents],
    tenure,
    MonthlyCharges,
    TotalCharges
]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success("Customer will Churn!" if prediction[0] else "Customer will Stay.")
