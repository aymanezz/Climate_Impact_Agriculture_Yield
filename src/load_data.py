# load_data.py
import pandas as pd

# Load the cleaned data
production = pd.read_csv('data/final/cleaned_production.csv')
temp_change = pd.read_csv('data/final/cleaned_temperature_change.csv')
land_cover = pd.read_csv('data/final/cleaned_land_cover.csv')
sea_level = pd.read_csv('data/final/cleaned_sea_level.csv')
atmospheric = pd.read_csv('data/final/cleaned_atmospheric.csv')

# Save loaded data to disk to be used by other scripts
production.to_csv('data/processed/production.csv', index=False)
temp_change.to_csv('data/processed/temp_change.csv', index=False)
land_cover.to_csv('data/processed/land_cover.csv', index=False)
sea_level.to_csv('data/processed/sea_level.csv', index=False)
atmospheric.to_csv('data/processed/atmospheric.csv', index=False)
