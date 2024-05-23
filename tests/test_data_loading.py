import unittest
from src.data.data_loader import load_data

class DataLoadingTestCase(unittest.TestCase):
    def test_load_data(self):
        data = load_data('tests/sample_data.csv')
        self.assertEqual(len(data), 100)  # Assuming sample_data.csv has 100 rows

if __name__ == '__main__':
    unittest.main()
