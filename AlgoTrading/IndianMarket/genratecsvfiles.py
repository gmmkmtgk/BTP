import datetime
from datetime import timedelta, date
import calendar
import datefuctions as df
from nsepy.history import get_price_list

def genratezips():
    #day
    try:
        ptoday = get_price_list(df.today())
        ptoday.to_csv(r'/home/keshav/Desktop/Prices/today.csv')
    except Exception as e:
        print("today " )
        print(e)
        d = 1
        if calendar.day_name[date.today().weekday()] == 'Monday':
            d = 3
        ptoday = get_price_list(df.today() + timedelta(days=-1*d))
        ptoday.to_csv(r'/home/keshav/Desktop/Prices/today.csv')

    #week
    try:
        pweek = get_price_list(df.week())
        pweek.to_csv(r'/home/keshav/Desktop/Prices/week.csv')
    except Exception as e:
        print("week" )
        print(e)
    #month
    try:
        pmonth = get_price_list(df.month())
        pmonth.to_csv(r'/home/keshav/Desktop/Prices/month.csv')
    except Exception as e:
        print("month " )
        print(e)
    #3month
    try:
        pthreemonth = get_price_list(df.threemonth())
        pthreemonth.to_csv(r'/home/keshav/Desktop/Prices/threemonth.csv')
    except Exception as e:
        print("tthreemonth ")
        print(e)
    #6month
    try:
        psixmonth = get_price_list(df.sixmonth())
        psixmonth.to_csv(r'/home/keshav/Desktop/Prices/sixmonth.csv')
    except Exception as e:
        print("sixmonth " )
        print(e)
    #year
    try:
        pyear = get_price_list(df.year())
        pyear.to_csv(r'/home/keshav/Desktop/Prices/year.csv')
    except Exception as e:
        print("yaer ")
        print(e)