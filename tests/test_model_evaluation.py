import unittest
from sklearn.metrics import mean_squared_error
from src.models.supervised.regression_model import RegressionModel

class ModelEvaluationTestCase(unittest.TestCase):
    def test_model_evaluation(self):
        model = RegressionModel()
        X = [[1, 2], [3, 4], [5, 6]]
        y = [1, 2, 3]
        model.train(X, y)
        predictions = model.predict(X)
        mse = mean_squared_error(y, predictions)
        self.assertLess(mse, 1.0)

if __name__ == '__main__':
    unittest.main()
