# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 06:31:17 2024

@author: DEANESH
"""

import os
import pandas as pd
import numpy as np

def remean_points(row):
    row.points = row.points - review_points_mean
    return row 

def my_datafram():
    # Fetch file data using the current dir path
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "A.csv"))
    
    print(df)
    
    print(df.loc[(df.A == 'A') & (df.B == 98)])
    print("----------")
    print(df.loc[(df.A == 'A') | (df.B >= 98)])
    print("----------")
    print(df.loc[df.A.isin(['A'])])
    print("----------")
    print(df.loc[df.C.notnull()])

    df = pd.DataFrame(np.random.randn(5, 4), columns=list('ABCD'), index=[0,1,2,3,4])
    df_1 = pd.DataFrame(np.random.randn(5, 4), columns=list('ABCD'), index=[0,1,2,3,4])
    
    df1 = df + df_1
    
    df1.to_csv(os.path.join(os.path.dirname(__file__), "Random.csv"))
    print("----------")
    print(df1)
    my_series = pd.Series(np.random.randint(2,7))
    print("----------")
    print(df.A.unique())


    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "Sample.csv"))
    # 87, 87, 100, 90, 90, 90
    print(df.points.median())

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "Sample.csv"))
print(df['points', 'country'])





