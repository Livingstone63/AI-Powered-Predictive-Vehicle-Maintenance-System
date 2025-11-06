import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

# --- Load Model ---
model = joblib.load("models/predictive_model.pkl")

# --- Load Data ---
data = pd.read_csv("data/vehicle_data.csv")

st.set_page_config(page_title="🚗 Predictive Vehicle Maintenance", layout="wide")

st.title("🚗 AI-Based Predictive Vehicle Maintenance System")
st.markdown("### Monitor vehicle health and schedule maintenance proactively")

# Sidebar filters
st.sidebar.header("⚙️ Filter Vehicles")
min_temp = st.sidebar.slider("Min Engine Temp (°C)", 70, 140, 70)
max_temp = st.sidebar.slider("Max Engine Temp (°C)", 70, 140, 140)

filtered_data = data[(data["engine_temp"] >= min_temp) & (data["engine_temp"] <= max_temp)]

# --- Prediction Function ---
def predict_failure(vehicle_row):
    X = np.array([[vehicle_row["engine_temp"], vehicle_row["vibration"], vehicle_row["mileage"], vehicle_row["brake_wear"]]])
    return model.predict(X)[0]

# --- Add Predictions to Data ---
filtered_data["predicted_failure"] = filtered_data.apply(predict_failure, axis=1)
filtered_data["status"] = filtered_data["predicted_failure"].apply(lambda x: "⚠️ Needs Service" if x == 1 else "✅ Healthy")

# --- Display Table ---
st.subheader("📊 Vehicle Health Summary")
st.dataframe(filtered_data[["vehicle_id", "engine_temp", "vibration", "mileage", "brake_wear", "status"]])

# --- Visualization ---
st.subheader("📈 Vehicle Condition Overview")
fig, ax = plt.subplots()
colors = filtered_data["predicted_failure"].map({0: "green", 1: "red"})
ax.scatter(filtered_data["engine_temp"], filtered_data["vibration"], c=colors)
ax.set_xlabel("Engine Temperature (°C)")
ax.set_ylabel("Vibration Level")
ax.set_title("Vehicle Condition Analysis")
st.pyplot(fig)

# --- Statistics ---
healthy = sum(filtered_data["predicted_failure"] == 0)
faulty = sum(filtered_data["predicted_failure"] == 1)

col1, col2 = st.columns(2)
with col1:
    st.metric("✅ Healthy Vehicles", healthy)
with col2:
    st.metric("⚠️ At-Risk Vehicles", faulty)

st.markdown("---")
st.markdown("Developed by **Livingstone Joseph** 🧠")
