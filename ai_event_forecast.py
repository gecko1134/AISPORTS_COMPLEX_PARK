import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def run():
    st.title("📈 AI Event Forecast")

    st.write("Upload or use demo event data to forecast attendance based on weather, sport, and date.")

    uploaded = st.file_uploader("Upload your events CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_csv("events.csv")

    st.subheader("📋 Raw Data Preview")
    st.dataframe(df.head())

    # Prepare features
    df["weather_code"] = df["weather"].map({"Sunny": 2, "Cloudy": 1, "Rain": 0})
    df["sport_code"] = df["sport"].astype("category").cat.codes
    df["dayofweek"] = pd.to_datetime(df["date"]).dt.dayofweek

    X = df[["weather_code", "sport_code", "dayofweek"]]
    y = df["expected_attendance"]

    # Train model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    st.subheader("📊 Prediction Results")
    result_df = pd.DataFrame({
        "Actual": y_test.values,
        "Predicted": predictions.astype(int)
    }).reset_index(drop=True)

    st.line_chart(result_df)

    mae = mean_absolute_error(y_test, predictions)
    st.metric("Mean Absolute Error", f"{mae:.2f} attendees")