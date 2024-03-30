
import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMRegressor
import joblib

# Load dataset
df = pd.read_csv('ElectricCarData_Clean.csv')

# Selecting relevant features and the target variable
X = df[['AccelSec', 'TopSpeed_KmH', 'Efficiency_WhKm']]
y = df['Range_Km']

# Splitting the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training a LightGBM model
model = LGBMRegressor()
model.fit(X_train, y_train)

# Saving the model and the test set for later use to the sdsds
joblib.dump(model, 'electric_car_model.joblib')
X_test.to_csv('X_test.csv', index=False)
y_test.to_csv('y_test.csv', index=False)

print("Model training complete and model saved")
