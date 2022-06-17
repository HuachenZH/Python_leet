# Brogrammer:
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num==0:
            return True
        return num%10!=0

# Programmer:
class Solution2:
    def isSameAfterReversals(self, num: int) -> bool:
        # the string approach will be faster... i suppose
        return int(str(int(str(num)[::-1]))[::-1])==num
        #              |------------------|          --> first reverse
        #      |------|                    |-----|   --> second reverse
sol=Solution2()
print(sol.isSameAfterReversals(1200))

