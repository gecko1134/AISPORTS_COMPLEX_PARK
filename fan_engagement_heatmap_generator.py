import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    st.title("📣 Fan Engagement Heatmap Generator")

    uploaded = st.file_uploader("Upload fan_interactions.csv", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        zones = ["Lobby", "Main Court", "Stadium Gate", "Kiosk Area", "App Usage", "VIP Lounge"]
        df = pd.DataFrame({
            "location": np.random.choice(zones, 300),
            "hour": np.random.randint(6, 23, 300),
            "interactions": np.random.randint(1, 100, 300)
        })

    st.subheader("📋 Engagement Records")
    st.dataframe(df.head())

    pivot = df.groupby(["location", "hour"])["interactions"].sum().unstack().fillna(0)

    st.subheader("🔥 Engagement Heatmap by Location & Hour")
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu", ax=ax)
    ax.set_title("Fan Interactions by Zone and Hour")
    st.pyplot(fig)

    zone_summary = df.groupby("location")["interactions"].sum().sort_values(ascending=False).reset_index()
    st.subheader("📍 Top Fan Interaction Zones")
    st.dataframe(zone_summary)