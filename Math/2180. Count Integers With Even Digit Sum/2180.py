class Solution:
    def digitSum(self,n:int) -> int:
        table=[]
        # get the one digit
        table.append(n%10)
        # get the other digits
        for i in range(len(str(n))-1):
            n=(n-table[len(table)-1])/10
            table.append(int(n%10))
        return sum(table)

    def countEven(self, num: int) -> int:
        # cf 1281 get all digits of a number
        count=0
        for i in range(1,num+1):
            # if the digit sum is even
            if self.digitSum(i)%2==0:
                count-=-1
        return count

sol=Solution()
print(sol.countEven(30))

