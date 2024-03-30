import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from . import common_setup

# Assuming your scripts are named train_model.py and visualize_predictions.py
import train_model
import visualize_predictions

class TrainModelTestCase(unittest.TestCase):
    def setUp(self):
        common_setup()

    @patch('pandas.read_csv')
    @patch('joblib.dump')
    def test_train_model(self, mock_dump, mock_read_csv):
        # Mock reading the CSV file
        df = pd.DataFrame({
            'AccelSec': [3.2, 4.5, 2.8],
            'TopSpeed_KmH': [180, 150, 160],
            'Efficiency_WhKm': [200, 190, 210],
            'Range_Km': [300, 250, 280]
        })
        mock_read_csv.return_value = df
        

        # Execute the script (this is a simplification; in reality, you might want to call a specific function instead)
        with patch('train_model.print') as mock_print:
            train_model.run_training()  # Assuming you encapsulate the script's functionality in a function
        
        # Check that the model and datasets were attempted to be saved
        self.assertTrue(mock_dump.called)
        mock_print.assert_called_with("Model training complete and model saved")

class VisualizePredictionsTestCase(unittest.TestCase):

    @patch('pandas.read_csv')
    @patch('joblib.load')
    @patch('matplotlib.pyplot.show')
    def test_visualize_predictions(self, mock_show, mock_load, mock_read_csv):
        # Mock loading the model and data
        model = MagicMock()
        model.predict.return_value = [290, 260, 270]  # Dummy predictions
        mock_load.return_value = model
        
        X_test = pd.DataFrame({
            'AccelSec': [3.2, 4.5, 2.8],
            'TopSpeed_KmH': [180, 150, 160],
            'Efficiency_WhKm': [200, 190, 210]
        })
        y_test = pd.Series([300, 250, 280])
        
        mock_read_csv.side_effect = [X_test, y_test]  # First call returns X_test, second returns y_test

        # Execute the script (this is a simplification; in reality, you might want to call a specific function instead)
        with patch('visualize_predictions.print') as mock_print:
            visualize_predictions.run_visualization()  # Assuming you encapsulate the script's functionality in a function
        
        # Check that the plot show method was called
        self.assertTrue(mock_show.called)
        mock_print.assert_called_with("Data Visualization started")

if __name__ == '__main__':
    unittest.main()
