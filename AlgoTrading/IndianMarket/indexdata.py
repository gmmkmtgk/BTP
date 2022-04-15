#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
There are currently 50+ indices maintained by NSE. You can get historical data for all of them.
get_history() missing 2 required positional arguments: 'start' and 'end'
"""

from nsepy import get_history
from datetime import date

nifty_next50 = get_history(symbol="NIFTY NEXT 50",
                            start=date(2015,1,1),
                            end=date(2015,1,10),
                            index=True)

print(nifty_next50)

nifty_eq_wt = get_history(symbol="NIFTY50 EQUAL WEIGHT",
                            start=date(2021,6,1),
                            end=date(2021,6,10),
                            index=True)

print(nifty_eq_wt)

vix = get_history(symbol="INDIAVIX",
            start=date(2021,1,1),
            end=date(2021,10,24),
            index=True)

vix[['Close']].plot()