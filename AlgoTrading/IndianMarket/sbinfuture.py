from datetime import date
from nsepy import get_history
# Stock futures (Similarly for index futures, set index = True)
stock_fut1 = get_history(symbol="SBIN",
                        start=date(2015,1,1),
                        end=date(2015,1,10),
                        futures=False,
                        expiry_date=date(2015,1,29))


stock_fut2 = get_history(symbol="SBIN",
                        start=date(2015,1,1),
                        end=date(2015,1,10),
                        futures=True,
                        expiry_date=date(2015,1,29))


ax = stock_fut1[['Close']].plot()
stock_fut2[['Close']].plot(ax = ax)
