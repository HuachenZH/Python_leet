class Solution:
    # ver ??
    # according to leetcode, there is solution without loops

    # ver alpha
    # surprisingly, the performance of this ver is not bad
    # runtime 23 ms 98.76%
    # memory 13.8 MB 91.56%
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n > 1:
            n /= 4
            if n % 1 != 0:
                return False
            # prepare for next iteration
            # nothing to do for the next iteration
            

        return True

epsi = Solution()
print(epsi.isPowerOfFour(-64))
