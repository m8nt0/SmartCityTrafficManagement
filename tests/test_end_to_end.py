import unittest
from src.main import main
from deployment.api.api_endpoints import app

class EndToEndTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_end_to_end(self):
        # Run main function
        try:
            main()
        except Exception as e:
            self.fail(f"Main function failed with error: {e}")

        # Test API
        response = self.app.post('/predict', json={'data': [1, 2, 3]})
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', response.get_json())

if __name__ == '__main__':
    unittest.main()
