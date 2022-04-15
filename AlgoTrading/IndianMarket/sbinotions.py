#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date
from nsepy import get_history

stock_opt = get_history(symbol="SBIN",
                        start=date(2015,1,1),
                        end=date(2015,1,10),
                        option_type="CE",
                        strike_price=300,
                        expiry_date=date(2015,1,29))

print(stock_opt)

data = stock_opt

data[['Close']].plot()