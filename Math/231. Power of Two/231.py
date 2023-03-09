class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n > 1:
            n /= 2
            if n % 1 != 0:
                return False
            # prepare for next iteration
            # nothing to do for the next iteration
            

        return True

epsi = Solution()
print(epsi.isPowerOfTwo(64))