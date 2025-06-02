import streamlit as st
import pandas as pd

class DemandForecaster:
    def __init__(self):
        self.model_name = "Demo Forecaster"

    def predict(self, df):
        df['predicted_users'] = df['hour'] * 5 + 100  # Fake formula
        return df

def run():
    st.title("Demand Forecast")
    st.write("Upload a CSV file with an 'hour' column (0–23) to simulate forecasting.")

    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        if 'hour' not in df.columns:
            st.error("CSV must contain 'hour' column.")
            return
        model = DemandForecaster()
        result = model.predict(df)
        st.success("Forecast complete.")
        st.dataframe(result)
        st.line_chart(result.set_index('hour')['predicted_users'])
    else:
        st.info("Upload a CSV with hourly data.")