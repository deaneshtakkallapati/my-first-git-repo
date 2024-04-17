# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 06:31:17 2024

@author: DEANESH
"""

import os
import pandas as pd
import numpy as np

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "Sample.csv"))
my_series = pd.Series(np.random.randint(2,7))
countries_reviewed = df.groupby(['country', 'province']).description.agg([len])

def remean_points(row):
    row.points = row.points - review_points_mean
    return row 

def my_datafram():
    # Fetch file data using the current dir path
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "A.csv"))
    
    print(df)    
    print(df.loc[(df.A == 'A') & (df.B == 98)])
    print(df.loc[(df.A == 'A') | (df.B >= 98)])
    print(df.loc[df.A.isin(['A'])])
    print(df.loc[df.C.notnull()])
    print(df.A.unique())
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











