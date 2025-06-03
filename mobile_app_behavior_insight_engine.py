import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    st.title("📱 Mobile App Behavior Insight Engine")

    uploaded = st.file_uploader("Upload app_usage_logs.csv", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        features = ["Check-In", "Book Class", "Chat", "View Schedule", "Shop", "Tutorial"]
        df = pd.DataFrame({
            "feature": np.random.choice(features, 300),
            "tier": np.random.choice(["Silver", "Gold", "VIP"], 300),
            "uses": np.random.randint(1, 40, 300)
        })

    st.subheader("📋 App Usage Records")
    st.dataframe(df.head())

    pivot = df.groupby(["feature", "tier"])["uses"].sum().unstack().fillna(0)

    st.subheader("📊 Feature Usage by Tier")
    fig, ax = plt.subplots(figsize=(10, 5))
    pivot.plot(kind="bar", stacked=True, ax=ax)
    ax.set_title("App Feature Usage by Tier")
    ax.set_ylabel("Total Uses")
    st.pyplot(fig)

    top_features = df.groupby("feature")["uses"].sum().sort_values(ascending=False).reset_index()
    st.subheader("🏆 Top App Features Overall")
    st.dataframe(top_features)