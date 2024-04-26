import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score

class CrossValidationMLExample:
    def __init__(self):
        print("Constructor - Start")
        print("Constructor - End")

    def main(self):
        print("Main - Start")
        data = pd.read_csv('melb_data.csv')
        y = data.Price
        # Select subset of predictors
        cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
        X = data[cols_to_use]

        my_pipeline = Pipeline(steps=[('imputer', SimpleImputer()),
                                      ('model', RandomForestRegressor(n_estimators=30, random_state=0))])

        # Note: scoring string has to be same. It fails if we dont enter string properly
        score = -1 * cross_val_score(my_pipeline, X, y,cv=5, scoring='neg_mean_absolute_error' )
        print("=====================")
        print("MAE: CrossValidation approach value is : %s " % str(score))
        print("Main - End")


if __name__ == "__main__":
    cross_validation = CrossValidationMLExample()
    cross_validation.main()