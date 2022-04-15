from nsepy import get_history
from datetime import date
from nsepy.derivatives import get_expiry_date


for i in range(12):
    i = i + 1
    expiry = get_expiry_date(year=2021, month=i)   
    print(expiry)

'''
stock_opt = get_history(symbol="SBIN",
                            start=date(2021,10,1),
                            end=date(2021,10,22),
                            futures=True,
                            expiry_date=date(2021, 10, 28))


print(stock_opt)
'''