import streamlit as st
import pandas as pd
import joblib

model = joblib.load('LogiReg_Heart.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')  


st.title("Heart Stroke Prediction by Uddipta :)")
st.markdown("Provide The Following Details")

age = st.slider("Age", 18, 100, 25)
sex = st.selectbox("SEX", ['Male', 'Female'])
ChestPainType = st.selectbox("Chest Pain Type", [ 'ATA', 'NAP', 'TA','ASY'])
RestingBP = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
Cholesterol = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)
FastingBS = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ['Yes', 'No'])
RestingECG = st.selectbox("Resting ECG", ['Normal', 'ST', 'LVH'])
MaxHR = st.slider("Maximum Heart Rate Achieved", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Induced Angina", ['Yes', 'No'])
Oldpeak = st.number_input("Oldpeak (ST depression induced by exercise)", 0.0, 10.0, 1.0)
ST_Slope = st.selectbox("ST Slope", ['Up', 'Flat', 'Down'])

if st.button("Predict"):
    input_data = pd.DataFrame({
        'Age': [age],
        'RestingBP': [RestingBP],
        'Cholesterol': [Cholesterol],
        'FastingBS': [1 if FastingBS == 'Yes' else 0],
        'RestingECG': [1 if RestingECG == 'Normal' else 2 if RestingECG == 'ST' else 3],
        'MaxHR': [MaxHR],
        'ExerciseAngina': [1 if exercise_angina == 'Yes' else 0],
        'Oldpeak': [Oldpeak],
        'ST_Slope': [1 if ST_Slope == 'Up' else 2 if ST_Slope == 'Flat' else 3]
    })

    input_df = input_data

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error("High Risk of Heart Stroke")
    else:
        st.success("Low Risk of Heart Stroke")
