# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 06:31:17 2024
@author: DEANESH
"""
import os
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


def ml_prediction_dataframe():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "melb_data.csv"))
    melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
    X = df[melbourne_features];  y = df.Price
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
    # Define model
    melbourne_model = DecisionTreeRegressor()
    melbourne_model.fit(train_X, train_y)
    # get predicted prices on validation data
    val_predictions = melbourne_model.predict(val_X)
    print(mean_absolute_error(val_y, val_predictions))


def process_dummy_dataframe():
    # Fetch file data using the current dir path
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "A.csv"))
    print(df.loc[(df.A == 'A') & (df.B == 98)])
    print(df.loc[(df.A == 'A') | (df.B >= 98)])
    print(df.loc[df.A.isin(['A'])])
    print(df.loc[df.C.notnull()])
    print(df.A.unique())
    return df


def my_dataframe():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "Sample.csv"))
    countries_reviewed = df.groupby(['country', 'province']).description.agg([len])
    # Median
    print(df.points.median())
    print(df.groupby(['points']).points.count())
    print(df.groupby(['points']).price.max()) 
    print(type(df.groupby(['winery']).apply(lambda df: df.title.iloc[0])))
    print(df.groupby(['country', 'price', 'taster_twitter_handle']).points.agg([len, min, max]))
    print(df.groupby(['country','province']).apply(lambda df: df.loc[df.points.idxmax()]))
    print(countries_reviewed)
    print(countries_reviewed.index)
    print(countries_reviewed.reset_index())
    print(countries_reviewed.reset_index().sort_values(by= 'len', ascending=False))
    print(countries_reviewed.sort_index())
    print(countries_reviewed.sort_values(by=['country', 'len']))


# ml_prediction_dataframe()




















