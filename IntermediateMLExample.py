import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
class IntermediateMLExample:
    def __init__(self):
        print("Constructor...")

    def main(self):
        print("Main...")
        inter_ml_example()

def inter_ml_example():
    # Read the data
    X_full = pd.read_csv('train.csv', index_col='Id')
    X_test_full = pd.read_csv('test.csv', index_col='Id')
    # print(X_full.columns)
    # print(X_test_full)

    # Obtain target and predictors
    y = X_full.SalePrice
    features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
    X = X_full[features].copy()
    X_test = X_test_full[features].copy()

    # Break off validation set from training data
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                          random_state=0)

    # Define the models
    model_1 = RandomForestRegressor(n_estimators=50, random_state=0)
    model_2 = RandomForestRegressor(n_estimators=100, random_state=0)
    model_3 = RandomForestRegressor(n_estimators=100, criterion='absolute_error', random_state=0)
    model_4 = RandomForestRegressor(n_estimators=200, min_samples_split=20, random_state=0)
    model_5 = RandomForestRegressor(n_estimators=100, max_depth=7, random_state=0)

    models = [model_1, model_2, model_3, model_4, model_5]
    mae_dict = {}
    for i in range(0, len(models)):
        mae_dict["model_"+str(i+1)] = score_model(models[i], X_train, X_valid, y_train, y_valid)
    mae_dict_keys = list(mae_dict.keys())
    mae_dict_values = list(mae_dict.values())
    min_mae_val = min(mae_dict_values)
    min_model_value = mae_dict_values.index(min_mae_val)
    print("Model Value: [%s] , MAE Value: [%s] " % (str(mae_dict_keys[min_model_value]), str(min_mae_val)))
    # Assign Best Model
    best_model = RandomForestRegressor(n_estimators=100, criterion='absolute_error', random_state=0)
    best_model.fit(X, y)
    preds_y = best_model.predict(X_test)
    # Save predictions in format used for competition scoring
    output = pd.DataFrame({'Id': X_test.index, 'SalePrice': preds_y})
    print(output)
    output.to_csv('submission.csv', index=False)


def score_model(model, X_t, X_v, y_t, y_v):
    model.fit(X_t, y_t)
    preds = model.predict(X_v)
    return mean_absolute_error(y_v, preds)


if __name__ == "__main__":
    inter_ml_ex = IntermediateMLExample()
    inter_ml_ex.main()
