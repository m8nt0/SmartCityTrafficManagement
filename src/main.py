from src.data.data_loader import load_data
from src.data.data_preprocessing import preprocess_data
from src.models.supervised.regression_model import RegressionModel

def main():
    # Load and preprocess data
    data = load_data('data/traffic_data.csv')
    X, y = preprocess_data(data)
    
    # Train model
    model = RegressionModel()
    model.train(X, y)

    # Make predictions
    predictions = model.predict(X)
    print(predictions)

if __name__ == "__main__":
    main()
