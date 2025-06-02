import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    st.title("💰 AI Revenue Maximizer")

    uploaded = st.file_uploader("Upload revenue.csv", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_csv("revenue.csv")

    st.subheader("📋 Revenue Data")
    st.dataframe(df.head())

    df["category_code"] = df["category"].astype("category").cat.codes
    df["source_code"] = df["source"].astype("category").cat.codes
    df["dayofweek"] = pd.to_datetime(df["date"]).dt.dayofweek

    X = df[["category_code", "source_code", "dayofweek"]]
    y = df["amount"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = GradientBoostingRegressor()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    st.subheader("📈 Predicted vs. Actual Revenue")
    result_df = pd.DataFrame({
        "Actual": y_test.values,
        "Predicted": preds.astype(int)
    }).reset_index(drop=True)

    st.line_chart(result_df)

    mae = mean_absolute_error(y_test, preds)
    st.metric("Mean Absolute Error", f"${mae:.2f}")