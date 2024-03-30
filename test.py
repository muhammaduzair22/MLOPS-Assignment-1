import unittest
from Model import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.client = app.test_client()
        # Propagate the exceptions to the test client
        self.client.testing = True

    def test_train_endpoint(self):
        # Send a GET request to the train endpoint
        response = self.client.get('/train')
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the expected message
        self.assertIn('Model trained successfully!', response.json['message'])

    def test_visualize_endpoint(self):
        # Send a GET request to the visualize endpoint
        response = self.client.get('/visualize')
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the expected message
        self.assertIn('Visualization created successfully!', response.json['message'])

    # Add more test methods as needed to cover other parts of your application

if __name__ == '__main__':
    unittest.main()
