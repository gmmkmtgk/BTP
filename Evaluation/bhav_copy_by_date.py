import datetime
from datetime import timedelta, date
from nsepy.history import get_price_list

year = int(input('Enter a year '))
month = int(input('Enter a month '))
day = int(input('Enter a day '))
my_date = datetime.date(year, month, day)
my_date = date(2022, 4, 13)
ptoday = get_price_list(my_date)
print(ptoday)