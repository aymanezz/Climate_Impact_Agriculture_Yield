# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load feature-engineered data
df = pd.read_csv('data/processed/feature_engineered_production.csv')

# Define features and target
X = df.drop(columns=['production'])
y = df['production']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
import joblib
joblib.dump(model, 'models/random_forest_model.pkl')
