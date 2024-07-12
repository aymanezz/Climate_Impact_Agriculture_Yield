# eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define function for loading data
def load_data(file_path):
    return pd.read_csv(file_path)

# Define function for inspecting data
def inspect_data(df):
    print(f"Shape of the dataframe: {df.shape}")
    print(f"Basic statistics:\n{df.describe()}")
    print(f"Missing values:\n{df.isna().sum()}")

# Load feature-engineered data
df = load_data('data/processed/feature_engineered_production.csv')

# Inspect the data
inspect_data(df)

# EDA: Visualize data distributions
def plot_distributions(df):
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()

plot_distributions(df)
