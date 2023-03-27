class Solution:
    # Runtime 1563 ms 22.25%
    # memory 13.9 MB 44.67%
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(1,x+1):
            if i*i > x:
                return i-1
        return -1

epsi = Solution()
print(epsi.mySqrt(24))
