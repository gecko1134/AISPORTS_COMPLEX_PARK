import streamlit as st
from ai_modules import demand_forecasting

def main():
    st.set_page_config(page_title="SportAI - Demand Forecast", layout="wide")
    st.sidebar.title("SportAI Suite")
    tool = st.sidebar.selectbox("Choose a module", ["Demand Forecast"])
    if tool == "Demand Forecast":
        demand_forecasting.run()

if __name__ == "__main__":
    main()