import datetime
from datetime import timedelta, date
import calendar
import datefuctions as df
from nsepy.history import get_price_list

def genratezips():
    #day
    try:
        ptoday = get_price_list(df.today())
        ptoday.to_csv(r'C:/Users/91941/OneDrive/Desktop/AT_MEGA/Prices/today.csv')
    except Exception as e:
        print("today " )

    #week
    try:
        pweek = get_price_list(df.week())
        pweek.to_csv(r'C:/Users/91941/OneDrive/Desktop/AT_MEGA/Prices/week.csv')
    except Exception as e:
        print("week" )
        #print(e)
    #month
    try:
        pmonth = get_price_list(df.month())
        pmonth.to_csv(r'C:/Users/91941/OneDrive/Desktop/AT_MEGA/Prices/month.csv')
    except Exception as e:
        print("month " )
        #print(e)
    #3month
    try:
        pthreemonth = get_price_list(df.threemonth())
        pthreemonth.to_csv(r'C:/Users/91941/OneDrive/Desktop/AT_MEGA/Prices/threemonth.csv')
    except Exception as e:
        print("tthreemonth ")
        #print(e)
    #6month
    try:
        psixmonth = get_price_list(df.sixmonth())
        psixmonth.to_csv(r'C:/Users/91941/OneDrive/Desktop/AT_MEGA/Prices/sixmonth.csv')
    except Exception as e:
        print("sixmonth " )
        #print(e)
    #year
    try:
        pyear = get_price_list(df.year())
        pyear.to_csv(r'C:/Users/91941/OneDrive/Desktop/AT_MEGA/Prices/year.csv')
    except Exception as e:
        print("year ")
        #print(e)

#genratezips()