import pandas as pd
import datefuctions as df
import datetime

now = datetime.datetime.now()
filename = 'result'  + 'NSE500' + str(df.today()) + str(now.hour) + str(now.minute) + str(now.second)

df1 = pd.read_csv (r'../NseIndex/NSE500.csv')
df2 = pd.read_csv (r'../Results/Result.csv')


df_inner = pd.merge(df2, df1,on='SYMBOL', how='inner')
print(df_inner['SYMBOL'])

df_inner['SYMBOL'].to_csv(r'../'+filename+'.csv')