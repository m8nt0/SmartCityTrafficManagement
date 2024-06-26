import unittest
from flask import Flask
from deployment.api.api_endpoints import app

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict_endpoint(self):
        response = self.app.post('/predict', json={'data': [1, 2, 3]})
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', response.get_json())

if __name__ == '__main__':
    unittest.main()
