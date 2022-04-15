#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 20:18:21 2021

@author: keshav
"""

from nsepy.history import get_history
from nsepy.history import get_price_list
from datetime import date
import pandas as pd

df1 = pd.read_csv ('today')

df1 = df1.loc[:, 'SYMBOL':'CLOSE']


df2 = pd.read_csv ('month')

df2 = df2.loc[:, 'SYMBOL':'CLOSE']



df1.drop('SERIES', inplace=True, axis=1)
df2.drop('SERIES', inplace=True, axis=1)
df1.drop('OPEN', inplace=True, axis=1)
df2.drop('OPEN', inplace=True, axis=1)
df1.drop('HIGH', inplace=True, axis=1)
df2.drop('HIGH', inplace=True, axis=1)
df1.drop('CLOSE', inplace=True, axis=1)
df2.drop('CLOSE', inplace=True, axis=1)

print(df2)
print(df1)
df_inner = pd.merge(df1, df2, on='SYMBOL', how='inner')


symlst = [] 
pricelst = []

for ind in df_inner.index:

     s = df_inner['LOW_x'][ind]/df_inner['LOW_y'][ind]
     symlst.append(s)
     
df_inner['Value'] = symlst
r = df_inner.sort_values(by=['Value'],ascending=False)
print(r)
print(r.head(100))
k = r.head(100)
k.to_csv('result.csv')
r.to_csv('final.csv')
r.to_csv(r'/home/keshav/Desktop/Prices/result.csv')




