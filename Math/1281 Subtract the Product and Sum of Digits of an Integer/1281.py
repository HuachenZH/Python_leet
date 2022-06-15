class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # get all the digits and add them into a list
        digitList=[]
        n_str=str(n)
        for i in range(len(n_str)):
            digitList.append(int(n_str[i]))
        # get the product and the sum
        product=1
        summ=0
        for digit in digitList:
            product*=digit
            summ+=digit
        # get the substraction
        result=product-summ
        return result
sol=Solution()
sol.subtractProductAndSum(125)


class Solution2:
    def getDigits(self,n:int) -> list:
        '''Get all the digits of a number and save them into a list.
        Pure Math approach.
        The return list will be [ones digit, tens digit, hundreds digti...] '''
        table=[]
        # get the one digit
        table.append(n%10)
        # get the other digits
        for i in range(len(str(n))-1):
            n=(n-table[len(table)-1])/10
            print(n)
            table.append(int(n%10))
        return table
sol2=Solution2()
print(sol2.getDigits(1234))
