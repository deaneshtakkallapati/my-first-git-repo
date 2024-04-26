import pandas as pd
# Regressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
# Metrics
from sklearn.metrics import mean_absolute_error
# Model Selection
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# Missing Values Approaches
class IntermediateMLExample:
    def __init__(self):
        print("Constructor...")

    def main(self):
        try:
            print("Main...")
            # inter_ml_example()
            missing_value_approaches()
        except Exception as ex:
            print("Exception occured : "+str(ex))


def missing_value_approaches():
    df = pd.read_csv('melb_data.csv')

    # Set X and y values
    y = df.Price

    melb_predictors = df.drop(['Price'], axis=1)
    X = melb_predictors.select_dtypes(exclude=['object'])
    X_train, X_valid, y_train, y_valid = train_test_split(X,y, train_size=0.8, test_size=0.2, random_state=0)

    ####################### Approach 1: Remove Columns - Start #########################
    # Find columns to remove
    cols_with_missing_values = [col for col in X_train.columns if X_train[col].isnull().any()]

    # Reduced Train and Test Data
    reduced_X_train = X_train.drop(cols_with_missing_values, axis=1)
    reduced_X_valid = X_valid.drop(cols_with_missing_values, axis=1)
    val = score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid)
    print("MAE from App 1: remove columns having null values : [%s] " % str(val))
    print("===================================================================")
    ####################### Approach 1: Remove Columns - Endd ########################

    ############# Approach 2: Add mean value to null Columns - Start #################
    imputer = SimpleImputer()

    #Impute Train and Test data
    impute_X_train = pd.DataFrame(imputer.fit_transform(X_train))
    impute_X_valid = pd.DataFrame(imputer.transform(X_valid))

    impute_X_train.columns = X_train.columns
    impute_X_valid.columns = X_valid.columns
    val = score_dataset(impute_X_train, impute_X_valid, y_train, y_valid)
    print("MAE from App 2: Add mean value to null column values : [%s] " % str(val))
    print("===================================================================")

    ############# Approach 2: Add mean value to null Columns - End ###################
    ### Approach 3: Add Extra Columns for cols having null values with True/False Filled - Start ###

    # Take backup of Train and Valid data
    X_train_copy = X_train.copy()
    X_valid_copy = X_valid.copy()

    cols_with_missing_values = [col for col in X_train_copy.columns if X_train_copy[col].isnull().any()]

    for col in cols_with_missing_values:
        X_train_copy[str(col)+"_was_missing"] = X_train_copy[col].isnull()
        X_valid_copy[str(col)+"_was_missing"] = X_valid_copy[col].isnull()

    # Imputer
    imputer = SimpleImputer()
    impute_X_train_copy = pd.DataFrame(imputer.fit_transform(X_train_copy))
    impute_X_valid_copy = pd.DataFrame(imputer.transform(X_valid_copy))

    # Put column names back
    impute_X_train_copy.columns = X_train_copy.columns
    impute_X_valid_copy.columns = X_valid_copy.columns

    val = score_dataset(impute_X_train_copy, impute_X_valid_copy, y_train, y_valid)
    print("MAE from App 3: Add extra column for col having null values : [%s] " % str(val))
    print("===================================================================")

    ### Approach 3: Add Extra Columns for cols having null values with True/False Filled - End ###



def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_valid)
    return mean_absolute_error(y_pred, y_valid)


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
