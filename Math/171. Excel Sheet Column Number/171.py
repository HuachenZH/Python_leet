class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle=columnTitle[::-1]
        res=0
        for i in range(len(columnTitle)):
            res+=(ord(columnTitle[i])-64)*26**i
        return res
epsilon=Solution()
print(epsilon.titleToNumber('BA')) # BA = 53

# Explanation --
# with ord()-64, A becomes 1, B becomes 2, Z becomes 26...
# BA is a number of "twenty-six-decimal" of two digits: B and A, B is 2, A is 1
# so BA = B * 26^1 + A * 26^0
#       = 2 * 26^1 + 1 * 26^0