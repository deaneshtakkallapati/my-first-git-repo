from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

import os
import pandas as pd


df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'melb_data.csv'))
y = df.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = df[melbourne_features]
train_X, val_X, train_y, val_y = train_test_split(X,y,random_state=0)
melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(train_X, train_y)
val_predictions = melbourne_model.predict(val_X)
delta = mean_absolute_error(val_y, val_predictions)
print(delta)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
val_predictions = forest_model.predict(val_X)
delta = mean_absolute_error(val_y, val_predictions)
print(delta)