#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 00:42:56 2021

@author: keshav
"""

from nsepy import get_rbi_ref_history
from datetime import date
rbi_ref = get_rbi_ref_history(date(2000,1,1), date(2021,1,24))

print(rbi_ref)

rbi_ref[['1 EURO']].plot()

