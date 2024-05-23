import unittest
from src.models.supervised.regression_model import RegressionModel

class TestModelTraining(unittest.TestCase):
    def test_train(self):
        model = RegressionModel()
        X = [[1, 2], [3, 4], [5, 6]]
        y = [1, 2, 3]
        model.train(X, y)
        self.assertTrue(model.model.coef_ is not None)

if __name__ == '__main__':
    unittest.main()
