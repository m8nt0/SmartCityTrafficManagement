from sklearn.linear_model import LinearRegression

class RegressionModel:
    def __init__(self, alpha=0.01, max_iter=1000):
        self.model = LinearRegression()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
