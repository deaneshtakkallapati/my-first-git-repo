# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 06:31:17 2024

@author: DEANESH
"""

import os
import pandas as pd
import numpy as np

# Fetch file data using the current dir path
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "A.csv"))

print(df)

# print("----------------------------")

# print(df.loc[(df.A == 'A') & (df.B == 98)])

# print(df.loc[(df.A == 'A') | (df.B >= 98)])

 
# print(df.loc[df.A.isin(['A'])])

 
print(df.loc[df.C.notnull()])


df = pd.DataFrame([[123,345]])


df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))

df.to_csv(os.path.join(os.path.dirname(__file__), "Random.csv"))
