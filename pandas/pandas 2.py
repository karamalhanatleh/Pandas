# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:40:47 2022

@author: KRM0201517
"""


import pandas as pd
data=pd.Series([2,3,3,4,5,5,6,7,77,88])
print(data.describe())

print('\n'*10)
data=pd.Series([7,7,8,9,5,0])
print(data.describe())
print(data.agg(['max', 'min','std','var']))
print('\n'*10)




data1=pd.Series([1,2,3,4], index=['a','b','c','d'])
data2=pd.Series({'a':1 , "b":2 ,'c':3 , 'd':4})
print(data1)
print(data2)

print(data1['a'])
print(data2['a'])

print('\n'*10)



a=pd.Index([1,3,5,7,9])
b=pd.Index([2,3,5,7,11])

print(a)
print(b)
print(a & b)
print(a | b)
print(a^ b )









