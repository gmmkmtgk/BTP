
def pfibo(i):
    if i == 0:
        return 1
    if i == 1:
        return 1
    return pfibo(i-1) + pfibo(i-2)

for i in range(15):
    print(pfibo(i))

for i in range(15):
    print(float(pfibo(i))*(7/5))
