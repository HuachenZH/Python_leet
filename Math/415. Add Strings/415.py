class Solution:
    # use ord to bypass int
    # runtime 483 ms 5%
    # memory 13.9 MB 80.34%
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = 0
        for i in range(len(num1)-1,-1,-1):
            n1 += (ord(num1[i])-48) * 10**(len(num1)-1-i)
        n2 = 0
        for i in range(len(num2)-1,-1,-1):
            n2 += (ord(num2[i])-48) * 10**(len(num2)-1-i)
        return str(n1+n2)

epsi = Solution()
print(epsi.addStrings("11","123"))
