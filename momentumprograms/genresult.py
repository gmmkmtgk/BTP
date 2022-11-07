import pandas as pd
import datefuctions as df
import datetime
def getresult(df_inner,ww,mw,tmw,smw,yw):
    #filename = cf.nfiles()
    now = datetime.datetime.now()
    filename = 'result' + str(df.today()) + str(now.hour) + str(now.minute) + str(now.second)
    symlst = [] 
    pricelst = []

    for ind in df_inner.index:

        s =float( ww)*(df_inner['tp'][ind]/df_inner['wp'][ind]) + mw*(df_inner['tp'][ind]/df_inner['mp'][ind]) + tmw*(df_inner['tp'][ind]/df_inner['tmp'][ind])  + smw*(df_inner['tp'][ind]/df_inner['smp'][ind] ) + yw*(df_inner['tp'][ind]/df_inner['yp'][ind] )
        symlst.append(s)
        
    df_inner['Value'] = symlst
    r = df_inner.sort_values(by=['Value'],ascending=False)
    r.to_csv(r'../Results'+filename+'.csv')
    r['SYMBOL'].to_csv(r'../Results/Result.csv')
    return r