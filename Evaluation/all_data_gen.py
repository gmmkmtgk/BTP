import datetime
from datetime import timedelta, date
from nsepy.history import get_price_list

def last_day_of_month(any_day):
    # this will never fail
    # get close to the end of the month for any day, and add 4 days 'over'
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
    return next_month - datetime.timedelta(days=next_month.day)

for month in range(1, 13):
    savedate = last_day_of_month(datetime.date(2017, month, 1))
    savedatestr = str(savedate)
    try:
        bhav = get_price_list(savedate)
        bhav.to_csv("C:/Users/91941/OneDrive/Desktop/AT_MEGA/Evaluation/Files/" + savedatestr + ".csv")
    except Exception as e1:
        try:
            savedate =savedate -  timedelta(1)
            savedatestr = str(savedate)
            bhav = get_price_list(savedate)
            bhav.to_csv("C:/Users/91941/OneDrive/Desktop/AT_MEGA/Evaluation/Files/" + savedatestr + ".csv")
        except Exception as e2:
            try:
                savedate =savedate -  timedelta(1)
                savedatestr = str(savedate)
                bhav = get_price_list(savedate)
                bhav.to_csv("C:/Users/91941/OneDrive/Desktop/AT_MEGA/Evaluation/Files/" + savedatestr + ".csv")
            except Exception as e3:
                try:
                    savedate =savedate -  timedelta(1)
                    savedatestr = str(savedate)
                    bhav = get_price_list(savedate)
                    bhav.to_csv("C:/Users/91941/OneDrive/Desktop/AT_MEGA/Evaluation/Files/" + savedatestr + ".csv")
                except Exception as e4:
                    print(e4)

    