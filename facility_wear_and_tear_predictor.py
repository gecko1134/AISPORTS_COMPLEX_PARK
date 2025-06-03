import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    st.title("🔧 Facility Wear and Tear Predictor")

    uploaded = st.file_uploader("Upload zone_traffic_logs.csv", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        zones = ["Turf A", "Turf B", "Court 1", "Court 2", "Locker Room", "Track"]
        df = pd.DataFrame({
            "zone": np.random.choice(zones, 300),
            "hour": np.random.randint(6, 22, 300),
            "foot_traffic": np.random.randint(5, 80, 300)
        })

    st.subheader("📋 Hourly Traffic Logs")
    st.dataframe(df.head())

    df["wear_score"] = df["foot_traffic"] * 1.5
    wear_pivot = df.groupby(["zone", "hour"])["wear_score"].sum().unstack().fillna(0)

    st.subheader("🔥 Wear Risk Heatmap")
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.heatmap(wear_pivot, annot=True, fmt=".0f", cmap="YlOrRd", ax=ax)
    ax.set_title("Predicted Wear by Zone & Hour")
    st.pyplot(fig)

    risk_summary = df.groupby("zone")["wear_score"].sum().sort_values(ascending=False).reset_index()
    st.subheader("⚠️ High-Risk Zones (Maintenance Priority)")
    st.dataframe(risk_summary)