class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num)%2!=0: return num
        else: # int(num) is even
            for i in range(len(num)-1,-1,-1):
                if int(num[i])%2!=0: # the digit is odd
                    return num[:i+1]
            return ''

epsilon=Solution()
print(epsilon.largestOddNumber("4206"))
