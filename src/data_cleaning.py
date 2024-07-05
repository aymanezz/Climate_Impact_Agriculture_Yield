import pandas as pd

# Load the datasets
canada_weather = pd.read_csv('../data/canada_weather.csv')
city_temperature = pd.read_csv('../data/city_temperature.csv')
rainfall_india = pd.read_csv('../data/rainfall_in_india_1901-2015.csv')
weather_data = pd.read_csv('../data/weather_data.csv')
weather_aus = pd.read_csv('../data/weatherAUS.csv')

# Handle missing values (example: filling with mean or dropping)
canada_weather.fillna(canada_weather.mean(), inplace=True)
city_temperature.fillna(city_temperature.mean(), inplace=True)
rainfall_india.fillna(rainfall_india.mean(), inplace=True)
weather_data.fillna(weather_data.mean(), inplace=True)
weather_aus.fillna(weather_aus.mean(), inplace=True)

# Remove duplicates if any
canada_weather.drop_duplicates(inplace=True)
city_temperature.drop_duplicates(inplace=True)
rainfall_india.drop_duplicates(inplace=True)
weather_data.drop_duplicates(inplace=True)
weather_aus.drop_duplicates(inplace=True)

# Save the cleaned datasets
canada_weather.to_csv('../data/cleaned_canada_weather.csv', index=False)
city_temperature.to_csv('../data/cleaned_city_temperature.csv', index=False)
rainfall_india.to_csv('../data/cleaned_rainfall_in_india.csv', index=False)
weather_data.to_csv('../data/cleaned_weather_data.csv', index=False)
weather_aus.to_csv('../data/cleaned_weather_aus.csv', index=False)

print("Data cleaning completed and cleaned datasets saved.")
