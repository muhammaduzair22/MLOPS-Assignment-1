import unittest
import os

from train_model import train_model_function
from visualize_predictions import visualize_predictions_function  # Import the function with the correct name

class TestTrainModel(unittest.TestCase):
    def test_train_model(self):
        # Run the train_model function
        train_model_function()
        # Check if the model file is created
        self.assertTrue(os.path.exists('electric_car_model.joblib'))
        # Check if the test data files are created
        self.assertTrue(os.path.exists('X_test.csv'))
        self.assertTrue(os.path.exists('y_test.csv'))

# class TestVisualizePredictions(unittest.TestCase):
#     def test_visualize_predictions(self):
#         # Run the visualize_predictions function
#         visualize_predictions_function()  # Use the function with the correct name
#         # Check if the plot file is created
#         self.assertTrue(os.path.exists('predictions_plot.png'))

if __name__ == '__main__':
    unittest.main()
