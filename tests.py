import pytest
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, r2_score


@pytest.fixture
def trained_model():
    # Load the trained model from the file
    model = joblib.load('model.pkl')
    return model


@pytest.fixture
def test_data():

    data = pd.read_csv('diamonds.csv')
    df = pd.DataFrame(data)

    test_X = df[['carat', 'depth', 'table','x','y','z']]
    test_y = df['price']

    return test_X, test_y


def test_mean_squared_error(trained_model, test_data):
    model = trained_model
    X_test, y_test = test_data

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)

    assert mse is not None
    assert mse >= 0


def test_r_squared_score(trained_model, test_data):
    model = trained_model
    X_test, y_test = test_data
    
    y_pred = model.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    
    assert r2 is not None
    assert 0 <= r2 <= 1
