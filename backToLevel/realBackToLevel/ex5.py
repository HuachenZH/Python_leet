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


def complet(a:int) -> bool:
    if '0' in str(a**2)+str(a**3):
        # return 45 == sum(list(dict.fromkeys( getDigits(a**2) + getDigits(a**3)  ))) # use dictionary to eliminate duplicates
        return 45 == sum(  list(  set(  getDigits(a**2) + getDigits(a**3)  )  )  )   # use set to eliminate duplicates
        # get all digits and eliminate duplicates. And compute the sum. If the sum equals 45, then it contains 1 to 9
    else:
        return False


print(complet(69))
