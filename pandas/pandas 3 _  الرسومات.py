# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 20:07:06 2022

@author: KRM0201517
"""

import pandas as pd


data=pd.Series((3,6,9,8,5,4,2,6,3,5,8))
print(data.describe())
'''
data.plot()
data.plot(kind='line')

'''



'''
data.plot(kind='pie')

'''



'''
data.plot(kind='bar')

'''



'''
data.plot(kind='barh')

'''

'''
# dd=pd.Series((1,2.5,5,2,2,3,4,5))
# dd.plot(kind='hist')
data.plot(kind='hist')

'''


'''
# d3=pd.Series([1,2,2,3,5,6])
# d3.plot(kind='box')
# print(d3.describe())

data.plot(kind='box')
'''


'''
#الكثاقه او التكرار
data.plot(kind='kde')

'''



'''
# d4=pd.Series([1,2,3,3])
# d4.plot(kind='area')
data.plot(kind='area')
'''



