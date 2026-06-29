import streamlit as st
import pickle
import pandas as pd
import numpy as np 
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🧪 Model Evaluation")

df = pd.read_csv("data/house_price_chennai_hyd_bangalore_realistic.csv")

# Create price categories
df["price_class"] = pd.cut(
    df["price_inr"],
    bins=[0, 6000000, 12000000, 30000000],
    labels=["Low", "Medium", "High"]
)

model = pickle.load(open("model/model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))
encoder = pickle.load(open("model/encoder.pkl", "rb"))

df["city"] = encoder.transform(df["city"])
X = df.drop(["price_inr", "price_class"], axis=1)
y = df["price_class"]

X_scaled = scaler.transform(X)
pred_prices = model.predict(X_scaled)

pred_class = pd.cut(
    pred_prices,
    bins=[0, 6000000, 12000000, 30000000],
    labels=["Low", "Medium", "High"]
)

cm = confusion_matrix(y, pred_class)

fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Low","Medium","High"],
            yticklabels=["Low","Medium","High"])
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")

st.pyplot(fig)
