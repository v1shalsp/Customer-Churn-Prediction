# Gender -> 1 Female    0 Male
# Churn -> 1 Yes     0 No
# Scaler is exported as scaler.pkl
# Model is exported as model.pkl
# Clmns in X -> 'Age', 'Gender', 'Tenure', 'MonthlyCharges'

import streamlit as st
import joblib
import numpy as np

scaler = joblib.load("scaler.pkl")
model = joblib.load("best_model.pkl")

st.title("Churn Prediction App")
st.write("This app predicts whether a customer will churn or not based on their information.")

st.divider()

st.write("Enter the values:")

st.divider()

age = st.number_input("Enter Age", min_value=18, max_value=100, value=30) 

gender = st.selectbox("Enter Gender", ["Male", "Female"])

tenure = st.number_input("Enter Tenure", min_value=0, max_value=150, value=12)

monthly_charges = st.number_input("Enter Monthly Charges", min_value=30, max_value=150, value=50)

st.divider()

pred_button = st.button("Predict")
if pred_button:
    gender_sel = 1 if gender == "Female" else 0
    
    X = [age, gender_sel, tenure, monthly_charges]
    X1 = np.array(X)
    X_scaled = scaler.transform([X1])
    
    pred = model.predict(X_scaled)
    
    predicted_churn = "Yes" if pred == 1 else "No"
    
    st.write(f"The predicted churn: {predicted_churn}")
    
else:
    st.write("Please enter the values and click on Predict to see the result.")
    st.stop()