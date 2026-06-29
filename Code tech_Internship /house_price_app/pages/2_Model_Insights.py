import streamlit as st
import pickle
import pandas as pd

st.title("📊 Feature Importance")

model = pickle.load(open("model/model.pkl", "rb"))
features = [
    "City", "Area (sqft)", "Bedrooms",
    "Bathrooms", "Age (years)", "Metro Distance"
]

importance = model.coef_

df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
}).sort_values(by="Importance", ascending=False)

st.bar_chart(df.set_index("Feature"))

st.info("Higher bar = stronger impact on price")
