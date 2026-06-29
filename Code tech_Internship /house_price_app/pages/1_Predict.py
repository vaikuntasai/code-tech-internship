import streamlit as st
import numpy as np
import pickle

st.title("🔮 Predict House Price")

# Load model objects
model = pickle.load(open("model/model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))
encoder = pickle.load(open("model/encoder.pkl", "rb"))

# Sidebar inputs
st.sidebar.header("🏠 House Details")

city = st.sidebar.selectbox("City", ["Chennai", "Hyderabad", "Bangalore"])
area = st.sidebar.slider("Area (sqft)", 300, 3000, 1000)
bedrooms = st.sidebar.selectbox("Bedrooms", [1, 2, 3, 4])
bathrooms = st.sidebar.selectbox("Bathrooms", [1, 2, 3, 4, 5])
age = st.sidebar.slider("House Age (years)", 0, 30, 10)
metro = st.sidebar.slider("Distance from Metro (km)", 0.1, 15.0, 5.0)

city_encoded = encoder.transform([city])[0]

input_data = np.array([[city_encoded, area, bedrooms, bathrooms, age, metro]])
input_scaled = scaler.transform(input_data)

if st.button("🚀 Predict Price"):
    price = model.predict(input_scaled)[0]
    st.success(f"💰 Estimated Price: ₹ {int(price):,}")
