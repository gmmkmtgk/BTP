#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 00:55:12 2021

@author: keshav
"""

from nsepy.history import get_price_list
from datetime import date
prices = get_price_list(dt=date(2021,10,22))

symdata = prices.loc[:,"SYMBOL"]

print(symdata)


prices.to_csv("symdata")