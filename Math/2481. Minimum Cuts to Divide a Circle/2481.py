class Solution:
    # i thought it would be much more complicate
    # runtime 31 ms 70.62%
    # memory 13.7 MB 91.88%
    def numberOfCuts(self, n: int) -> int:
        # it makes me think of recursive.
        # no wait it want equal slices
        if n == 1:
            return 0
        if n % 2 == 0: # if n is even
            return int(n/2)
        else: # else, n is odd
            return n
        

epsi = Solution()
print(epsi.numberOfCuts(5))
