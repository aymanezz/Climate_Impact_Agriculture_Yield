# feature_engineering.py
import pandas as pd

# Load merged data
production = pd.read_csv('data/processed/merged_production.csv')

# Creating lag features
for lag in [1, 3, 6]:
    production[f'Temperature Change_lag_{lag}'] = production.groupby('Area')['Temperature Change'].shift(lag)
    production[f'CO2concentration_lag_{lag}'] = production['CO2concentration'].shift(lag)

# Creating interaction features
production['Temperature Change_x_Land Cover'] = production['Temperature Change'] * production['Land Cover']
production['Temperature Change_x_CO2concentration'] = production['Temperature Change'] * production['CO2concentration']
production['Land Cover_x_CO2concentration'] = production['Land Cover'] * production['CO2concentration']

# Save the feature-engineered data to disk
production.to_csv('data/processed/feature_engineered_production.csv', index=False)
