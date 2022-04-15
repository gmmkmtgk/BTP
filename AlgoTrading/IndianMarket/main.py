import genratecsvfiles as gf
import gentable
import genresult
import countingfiles as cf

gf.genratezips()

df_inner = gentable.gen()
df_inner.to_csv(r'/home/keshav/Desktop/Tables/Table.csv')
genresult.getresult(df_inner,1,1,1,1,1)


