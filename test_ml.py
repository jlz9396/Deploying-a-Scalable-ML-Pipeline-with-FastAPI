import pytest
import os 
import logging 
import pickle
import pandas as pd

@pytest.fixture(scope="module")
def path():
    return "./data/census.csv"

@pytest.fixture(scope="module")
def data():
    # code to load in the data.
    datapath = "./data/census.csv"
    return pd.read_csv(datapath)

@pytest.fixture(scope="module")
def features():
    cat_features = [    "workclass",
                        "education",
                        "marital-status",
                        "occupation",
                        "relationship",
                        "race",
                        "sex",
                        "native-country"]
    return cat_features

## TODO: implement the first test. Change the function name and input as needed
def test_import_data(path):
    """
    Test presence and shape of dataset file
    """
    try:
        df = pd.read_csv(path)

    except FileNotFoundError as err:
        logging.error("File not found")
        raise err

    # Check the df shape
    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0

    except AssertionError as err:
        logging.error(
        "Testing import_data: The file doesn't appear to have rows and columns")
        raise err


## TODO: implement the second test. Change the function name and input as needed
def test_features(data, features):
    """
    Check that categorical features are in dataset
    """
    try:
        assert sorted(set(data.columns).intersection(features)) == sorted(features)
    except AssertionError as err:
        logging.error(
        "Testing dataset: Features are missing in the data columns")
        raise err


## TODO: implement the third test. Change the function name and input as needed
def test_is_model():
    """
    Check saved model is present
    """
    savepath = "./model/model.pkl"
    if os.path.isfile(savepath):
        try:
            _ = pickle.load(open(savepath, 'rb'))
        except Exception as err:
            logging.error(
            "Testing saved model: Saved model does not appear to be valid")
            raise err
    else:
        pass
