import numpy as np
def getDigits(n:int) -> list:
    '''Get all the digits of a number and save them into a list.
    Pure Math approach.
    The return list will be [ones digit, tens digit, hundreds digti...] '''
    table=[]
    # get the one digit
    table.append(n%10)
    # get the other digits
    for i in range(len(str(n))-1):
        n=(n-table[len(table)-1])/10
        table.append(int(n%10))
    return table
def arm_is_strong(n:int) -> bool:
    arr=np.array(getDigits(n))
    return n == np.power(arr,3).sum()
out=[]
for i in range(10000):
    if arm_is_strong(i):
        out.append(i)
print(out)
