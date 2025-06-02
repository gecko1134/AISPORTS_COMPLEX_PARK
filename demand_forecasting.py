
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib

class DemandForecaster:
    def __init__(self, model_path=None):
        if model_path:
            self.model, self.scaler = joblib.load(model_path)
        else:
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
            self.scaler = StandardScaler()

    def train(self, df, feature_cols, target_col):
        X = df[feature_cols]
        y = df[target_col]
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        joblib.dump((self.model, self.scaler), "demand_model.pkl")

    def predict(self, df):
        X_scaled = self.scaler.transform(df)
        return self.model.predict(X_scaled)
