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


print("ello")
df1 = pd.read_csv ('today')

#print(df1.loc[:, 'SYMBOL':'CLOSE'])


df2 = pd.read_csv ('month')

print(df2.loc[:, 'SYMBOL':'CLOSE'])

#df_row = pd.concat([df1, df2])


#print(df_row)

# pd.set_option("display.max_rows", False)
# pd.set_option("display.max_columns", False)
df_inner = pd.merge(df1, df2, on='SYMBOL', how='inner')

print(df_inner)

# symbols = df1.loc[:,"SYMBOL"]
# print(symbols)


symlst = [] 
pricelst = []