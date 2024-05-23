import unittest
from src.main import main

class IntegrationTestCase(unittest.TestCase):
    def test_integration(self):
        try:
            main()
        except Exception as e:
            self.fail(f"Integration test failed with error: {e}")

if __name__ == '__main__':
    unittest.main()
