import countingfiles as cf
import pandas as pd
import datefuctions as df
def getresult(df_inner,ww,mw,tmw,smw,yw):
    #filename = cf.nfiles()
    filename = str(df.today())
    symlst = [] 
    pricelst = []

    for ind in df_inner.index:

        s = ww*df_inner['tp'][ind]/df_inner['wp'][ind] + mw*df_inner['tp'][ind]/df_inner['mp'][ind] + tmw*df_inner['tp'][ind]/df_inner['tmp'][ind]  + smw*df_inner['tp'][ind]/df_inner['smp'][ind]  + yw*df_inner['tp'][ind]/df_inner['yp'][ind] 
        symlst.append(s)
        
    df_inner['Value'] = symlst
    r = df_inner.sort_values(by=['Value'],ascending=False)
    #print(r.head(100))
    r.to_csv(r'/home/keshav/Desktop/Results/Result.csv')
    r.to_csv(r'/home/keshav/Desktop/Results/'+filename+'.csv')
    return r