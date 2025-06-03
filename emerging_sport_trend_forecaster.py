import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.title("📈 Emerging Sport Trend Forecaster")

    uploaded = st.file_uploader("Upload program_participation.csv", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        sports = ["Pickleball", "Soccer", "Esports", "Swim", "Yoga"]
        df = pd.DataFrame({
            "month": np.tile(pd.date_range("2023-01-01", periods=12, freq="M"), len(sports)),
            "sport": np.repeat(sports, 12),
            "participants": np.random.randint(40, 500, 60)
        })

    st.subheader("📋 Monthly Sport Participation")
    st.dataframe(df.head())

    df["month"] = pd.to_datetime(df["month"])
    trend = df.groupby("sport")["participants"].apply(lambda x: x.pct_change().mean()).reset_index(name="avg_growth_rate")
    top_gainers = trend.sort_values("avg_growth_rate", ascending=False)

    st.subheader("📊 Emerging Sport Trends")
    st.dataframe(top_gainers)

    fig, ax = plt.subplots()
    for sport in df["sport"].unique():
        df[df["sport"] == sport].plot(x="month", y="participants", ax=ax, label=sport)
    ax.set_title("Sport Participation Over Time")
    st.pyplot(fig)