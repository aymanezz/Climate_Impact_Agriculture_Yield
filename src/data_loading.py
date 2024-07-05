import pandas as pd

# Load the datasets
canada_weather = pd.read_csv('../data/canada_weather.csv')
city_temperature = pd.read_csv('../data/city_temperature.csv')
rainfall_india = pd.read_csv('../data/rainfall_in_india_1901-2015.csv')
weather_data = pd.read_csv('../data/weather_data.csv')
weather_aus = pd.read_csv('../data/weatherAUS.csv')

# Display the first few rows of each dataset to inspect
print("Canada Weather Data:")
print(canada_weather.head(), "\n")

print("City Temperature Data:")
print(city_temperature.head(), "\n")

print("Rainfall in India (1901-2015):")
print(rainfall_india.head(), "\n")

print("Weather Data:")
print(weather_data.head(), "\n")

print("WeatherAUS Data:")
print(weather_aus.head(), "\n")

# Save the inspection result to a log file
with open('../docs/data_loading_log.txt', 'w') as log_file:
    log_file.write("Canada Weather Data:\n")
    log_file.write(canada_weather.head().to_string() + "\n\n")
    log_file.write("City Temperature Data:\n")
    log_file.write(city_temperature.head().to_string() + "\n\n")
    log_file.write("Rainfall in India (1901-2015):\n")
    log_file.write(rainfall_india.head().to_string() + "\n\n")
    log_file.write("Weather Data:\n")
    log_file.write(weather_data.head().to_string() + "\n\n")
    log_file.write("WeatherAUS Data:\n")
    log_file.write(weather_aus.head().to_string() + "\n\n")

print("Data loading completed and logged.")
