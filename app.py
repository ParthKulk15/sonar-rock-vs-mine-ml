import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("sonar_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Sonar Rock vs Mine Prediction")

st.write("Enter 60 sonar feature values:")

inputs = []
for i in range(60):
    val = st.number_input(f"Feature {i}", value=0.0)
    inputs.append(val)

if st.button("Predict"):
    X = np.array(inputs).reshape(1, -1)
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)[0]
    probability = model.predict_proba(X_scaled)[0][1]

    if prediction == 1:
        st.error(f"Mine detected ⚠️ (Confidence: {probability:.2f})")
    elif probability < 0.65:
         st.warning("⚠️ Low confidence prediction")
    else: 
         st.success(f"Rock detected ✅ (Confidence: {1 - probability:.2f})")
       
   

       
