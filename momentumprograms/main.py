import genratecsvfiles as gf
import gentable
import genresult

i = input("Press 1 for making fresh zip files else press 0\n")
if i == '1':
	gf.genratezips()

w = int(input("Enter week weight "))
m = int(input("Enter month weight "))
tm = int(input("Enter threemonth weight "))
sm = int(input("Enter sixmonth weight "))
y = int(input("Enter year weight "))

df_inner = gentable.gen()
df_inner.to_csv(r'C:/Users/91941/OneDrive/Desktop/AT_MEGA/Tables/Table.csv')

o = genresult.getresult(df_inner,w,m,tm,sm,y)

print(o)
#print(o.loc['SYMBOL'])

