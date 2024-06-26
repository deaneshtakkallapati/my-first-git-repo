import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

class PipelineInterMLExample:
    def __init__(self):
        print("Constructor.... Start")
        print("Constructor.... End")

    def main(self):
        print("Main.... Start")
        # Read the data
        data = pd.read_csv('melb_data.csv')
        X_train_full, X_valid_full, y_train, y_valid = self.divide_data_into_train_and_validation(data)
        categorical_cols, numerical_cols = self.get_columns(X_train_full)
        # Keep selected columns only
        my_cols = categorical_cols + numerical_cols
        X_train = X_train_full[my_cols].copy()
        X_valid = X_valid_full[my_cols].copy()

        numerical_transformer = SimpleImputer(strategy='constant')
        categorical_transformer = (
            Pipeline(steps=[('imputer', SimpleImputer(strategy='most_frequent')) ,
                            ('onehot', OneHotEncoder(handle_unknown='ignore'))]))

        preprocessor = (
            ColumnTransformer(transformers=[('num', numerical_transformer, numerical_cols),
                                            ('cat', categorical_transformer, categorical_cols)]))
        model = RandomForestRegressor(n_estimators=100, random_state=0)

        my_pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', model)])

        my_pipeline.fit(X_train, y_train)

        y_preds = my_pipeline.predict(X_valid)

        # Evaluate the model
        score = mean_absolute_error(y_valid, y_preds)
        print('MAE:', score)

        print("Main.... End")

    def divide_data_into_train_and_validation(self, data):
        # Separate target from predictors
        y = data.Price
        X = data.drop(['Price'], axis=1)
        # Divide data into training and validation subsets
        X_train_full, X_valid_full, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                                        random_state=0)
        return X_train_full, X_valid_full, y_train, y_valid

    def get_columns(self, X_train_full):
        # Select categorical columns with relatively low cardinality (convenient but arbitrary)
        categorical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].nunique() < 10 and
                            X_train_full[cname].dtype == "object"]
        # Select numerical columns
        numerical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].dtype in ['int64', 'float64']]
        return categorical_cols, numerical_cols


if __name__ == "__main__":
    pieline_ml_ex = PipelineInterMLExample()
    pieline_ml_ex.main()