class Solution:
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
            table.append(int(n%10))
        return table

    def testSelfDividing(self,n:int) ->bool:
        '''Test if an integer is self-dividing.'''
        # get all the digits of the int n
        digits=self.getDigits(n) # digits is a list

        for i in digits:
            if i==0: # An integer cannot modulo 0. So all numbers containing digit 0 is not self dividing
                return False
            if n%i!=0:
                return False
        return True


    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        res=[]
        for i in range(left,right+1):
            if self.testSelfDividing(i):
                res.append(i)
        return res
sol=Solution()
print(sol.selfDividingNumbers(1,22))

