import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    st.title("📉 Member Churn Prediction")

    uploaded = st.file_uploader("Upload members.csv", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_csv("members.csv")

    st.subheader("📋 Member Dataset")
    st.dataframe(df.head())

    df["days_since_join"] = (pd.to_datetime("2024-06-01") - pd.to_datetime(df["join_date"])).dt.days
    df["days_since_last"] = (pd.to_datetime("2024-06-01") - pd.to_datetime(df["last_visit"])).dt.days
    df["tier_code"] = df["tier"].astype("category").cat.codes
    df["status_label"] = (df["status"] == "Churned").astype(int)

    X = df[["age", "days_since_join", "days_since_last", "tier_code"]]
    y = df["status_label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    st.subheader("📊 Confusion Matrix")
    cm = confusion_matrix(y_test, preds)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Reds", ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    st.pyplot(fig)

    report = classification_report(y_test, preds, output_dict=True)
    st.subheader("📈 Classification Report")
    st.json(report)

    st.metric("Churned % in Sample", f"{100 * y.mean():.1f}%")