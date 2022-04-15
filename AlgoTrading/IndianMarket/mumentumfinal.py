#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 20:18:21 2021

@author: keshav
"""

from nsepy.history import get_history
from datetime import date
import pandas as pd 

df = pd.read_csv ('symdata')
# print(df)

# symbols = df.loc[:,"SYMBOL"]

# print(symbols)

symlst = [] 
pricelst = []


for ind in df.index:
     s = df['SYMBOL'][ind]
     symlst.append(s)
     data = get_history(symbol=s, start=date(2021,10,28), end=date(2021,10,28))
     pricelst.append(data.Close[0])
#print(symlst)

final = pd.DataFrame(symlst,columns = ['SYMBOL'])
final['Oct 28 2021' ] = pricelst
print(final)
final.to_csv('enjoy.csv')