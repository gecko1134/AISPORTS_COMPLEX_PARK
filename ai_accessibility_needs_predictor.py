import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def run():
    st.title("♿ AI Accessibility Needs Predictor")

    uploaded = st.file_uploader("Upload member_enrollments.csv", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        np.random.seed(42)
        df = pd.DataFrame({
            "member_id": [f"M{i}" for i in range(100)],
            "age": np.random.randint(6, 75, 100),
            "program": np.random.choice(["Yoga", "Swim", "Weights", "Cardio"], 100),
            "feedback_flag": np.random.choice([0, 1], 100, p=[0.85, 0.15]),
            "required_support": np.random.choice([0, 1], 100, p=[0.8, 0.2])
        })

    st.subheader("📋 Enrollment Data")
    st.dataframe(df.head())

    df["program_code"] = df["program"].astype("category").cat.codes
    X = df[["age", "program_code", "feedback_flag"]]
    y = df["required_support"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.25, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    st.subheader("📊 Prediction Report")
    preds = model.predict(X_test)
    report = classification_report(y_test, preds, output_dict=True)
    st.json(report)

    df["support_prob"] = model.predict_proba(X)[:, 1]
    st.subheader("🚩 Flagged Members for Support")
    st.dataframe(df[df["support_prob"] > 0.6][["member_id", "program", "support_prob"]])