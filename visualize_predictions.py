
import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load the saved model and test data
model = joblib.load('electric_car_model.joblib')
X_test = pd.read_csv('X_test.csv')
y_test = pd.read_csv('y_test.csv')
print("Data Visualization started")
# Making predictions
predictions = model.predict(X_test)

# Plotting actual vs. predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, alpha=0.7)
plt.xlabel('Actual Range (Km)')
plt.ylabel('Predicted Range (Km)')
plt.title('Actual vs. Predicted Car Ranges')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
plt.show()
