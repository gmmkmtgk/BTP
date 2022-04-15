#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 13:36:15 2021

@author: keshav


from nsepy import get_history 
from datetime import date
#from pylab import plot 

data = get_history(symbol = "SBIN", start=date(2021,10,1), end=date(2021,10,24))

print(data)

"""
from nsepy import get_history
from datetime import date
import pandas as pd
data = get_history(symbol="SBIN", start=date(2021,10,1), end=date(2021,10,25))
data.Close[0]

#data[['Close']].plot()

print(data)
"""
print(type(data))
row_1=data.iloc[0]
print(row_1)
data[['Close']].plot()
print(type(data))
data1 = data.loc[:,"Close"]
print(data1)
#data.to_csv('Index_Data_2020.csv', index=True)
"""