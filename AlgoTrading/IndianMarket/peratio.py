#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 00:18:35 2021

@author: keshav
"""

from nsepy import get_index_pe_history
from datetime import date

nifty_pe = get_index_pe_history(symbol="NIFTY",
                                start=date(2000,1,1),
                                end=date(2021,1,24))

#print(nifty_pe)
nifty_pe[['P/E']].plot()

nifty_pe.to_csv("niftype20years",)