class Solution:
    # Cf 2180 digitSum
    def digitSum(self,n:int) -> int:
        table=[]
        # get the one digit
        table.append(n%10)
        # get the other digits
        for i in range(len(str(n))-1):
            n=(n-table[len(table)-1])/10
            table.append(int(n%10))
        return sum(table)
    # solution: recursive
    def addDigitsr(self, num: int) -> int:
        if len(str(num))>1:
            return self.addDigits(self.digitSum(num))
        else:
            return num
    # solution: iterative
    def addDigitsi(self, num: int) -> int:
        while int(num/10)>0: # more than one digit
            num=self.digitSum(num)
        return num
epsilon=Solution()
print(epsilon.addDigitsr(38))
print(epsilon.addDigitsi(38))

