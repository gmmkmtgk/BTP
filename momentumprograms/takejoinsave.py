import countingfiles as cf
import pandas as pd
import datefuctions as df
import datetime

now = datetime.datetime.now()
filename = 'result'  + 'NSE500' + str(df.today()) + str(now.hour) + str(now.minute) + str(now.second)

df1 = pd.read_csv (r'C:/Users/91941/OneDrive/Desktop/AT_MEGA/NseIndex/NSE500.csv')
df2 = pd.read_csv (r'C:/Users/91941/OneDrive/Desktop/AT_MEGA/Results/Result.csv')


# df2.drop('LOW_x', inplace=True, axis=1)
# df2.drop('LOW_y', inplace=True, axis=1)
# df2.drop('Value', inplace=True, axis=1)

# ls1 = []clear
# ls2 = []


# for ind in df1.index:
#     ls1.append(ind)
# for ind in df2.index:
#     ls2.append(0)

# df1['new'] = ls1
# df2['new'] = ls2
# print(df1)
# print(df2)

df_inner = pd.merge(df2, df1,on='SYMBOL', how='inner')
print(df_inner['SYMBOL'])

df_inner['SYMBOL'].to_csv(r'C:/Users/91941/OneDrive/Desktop/AT_MEGA/Results/'+filename+'.csv')