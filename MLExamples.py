'''
STEPS to building and using a model are:
----------------------------------------
DEFINE: What type of model will it be? A decision tree? Some other type of model?
        Some other parameters of the model type are specified too.
FIT: Capture patterns from provided data. This is the heart of modeling.
PREDICT: Just what it sounds like
EVALUATE: Determine how accurate the model's predictions are.
'''
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

class MLExamples:
    def __init__(self):
        pass

    def main(self):
        start="Start"; end="End"
        print("========= Main Method.. {} ===============".format(start))
        ml_example_with_diff_models()
        print("========= Main Method.. {} ===============".format(end))


def ml_example_with_diff_models():
    # Read Melbourne House Prices...
    # Path of the file to read
    iowa_file_path = 'train.csv'

    home_data = pd.read_csv(iowa_file_path)
    # Create target object and call it y
    y = home_data.SalePrice
    # Create X
    features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
    X = home_data[features]

    # Split into validation and training data
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

    # Specify Model
    iowa_model = DecisionTreeRegressor(random_state=1)
    # Fit Model
    iowa_model.fit(train_X, train_y)

    # Make validation predictions and calculate mean absolute error
    val_predictions = iowa_model.predict(val_X)
    val_mae = mean_absolute_error(val_predictions, val_y)
    print("Decision Tree Model MAE without specifying max_leaf_nodes: {:,.0f}".format(val_mae))

    # Using best value for max_leaf_nodes
    iowa_model = DecisionTreeRegressor(max_leaf_nodes=100, random_state=1)
    iowa_model.fit(train_X, train_y)
    val_predictions = iowa_model.predict(val_X)
    val_mae = mean_absolute_error(val_predictions, val_y)
    print("Decision Tree Model MAE for best value of max_leaf_nodes: {:,.0f}".format(val_mae))

    # Define the model. Set random_state to 1
    rf_model = RandomForestRegressor(random_state=1)
    # fit your model
    rf_model.fit(train_X, train_y)
    # Calculate the mean absolute error of your Random Forest model on the validation data
    pred_y = rf_model.predict(val_X)
    rf_val_mae = mean_absolute_error(val_y, pred_y)
    print("Validation MAE for Random Forest Model: {}".format(rf_val_mae))


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    pred_y = model.predict(val_X)
    return mean_absolute_error(val_y, pred_y)


if __name__ == '__main__':
    m = MLExamples()
    m.main()
