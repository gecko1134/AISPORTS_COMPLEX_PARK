import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    st.title("📅 AI Scheduler Optimization Tool")

    uploaded = st.file_uploader("Upload bookings.csv", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_csv("bookings.csv")

    st.subheader("📋 Booking Data")
    st.dataframe(df.head())

    df["hour"] = df["time"].str.extract(r"(\d+):").astype(int)
    df["weekday"] = pd.to_datetime(df["date"]).dt.dayofweek
    df["sport_code"] = df["sport_type"].astype("category").cat.codes
    df["facility_id"] = df["facility_id"].astype(int)

    # Feature engineering
    df["target"] = (df["revenue"] > 50).astype(int)  # Simulate high-value slot

    X = df[["hour", "weekday", "sport_code", "facility_id"]]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    df["score"] = model.predict_proba(X)[:, 1]

    st.subheader("📈 Suggested High-Value Time Slots")
    st.write("Higher score = more likely to generate higher revenue bookings")

    pivot = df.pivot_table(index="hour", columns="weekday", values="score", aggfunc="mean")

    fig, ax = plt.subplots()
    sns.heatmap(pivot, annot=True, cmap="YlGnBu", ax=ax)
    ax.set_title("Score by Hour vs Weekday")
    ax.set_xlabel("Weekday (0=Mon)")
    ax.set_ylabel("Hour of Day")
    st.pyplot(fig)