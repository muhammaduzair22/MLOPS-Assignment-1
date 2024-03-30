import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np

@pytest.fixture
def mock_df():
    """Fixture for creating a mock DataFrame used in tests."""
    return pd.DataFrame({
        'AccelSec': [5.0, 6.0],
        'TopSpeed_KmH': [120, 150],
        'Efficiency_WhKm': [180, 190],
        'Range_Km': [300, 400]
    })

@patch('joblib.dump')
@patch('pandas.read_csv', return_value=mock_df())
def test_train_model(mock_read_csv, mock_dump, mock_df):
    """Test that the model is trained and saved correctly."""
    from train_model import df, X_train, y_train

    assert not df.empty
    assert all(col in X_train.columns for col in ['AccelSec', 'TopSpeed_KmH', 'Efficiency_WhKm'])
    mock_dump.assert_called_once()

@patch('matplotlib.pyplot.show')
@patch('joblib.load', return_value=MagicMock(predict=MagicMock(return_value=np.array([300, 400]))))
@patch('pandas.read_csv', return_value=mock_df())
def test_visualize_predictions(mock_read_csv, mock_load, mock_show, mock_df):
    """Test that predictions are made and the visualization is attempted."""
    from visualize_predictions import predictions

    assert len(predictions) == 2
    mock_load.return_value.predict.assert_called_once_with(mock_df()[['AccelSec', 'TopSpeed_KmH', 'Efficiency_WhKm']])
    mock_show.assert_called_once()
