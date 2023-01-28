# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:21:47 2022

@author: KRM0201517
"""

import pandas as pd
data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data)

print('\n'*5)
data = pd.Series((0.25, 0.5, 0.75, 1.0))
print(data.values)
print(data.index)
print(data.keys)