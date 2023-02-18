class Solution:
    # ver beta
    # after observing the output of version alpha,
    # we can find that the result is always n-1 (except for 1)
    def distinctIntegersBeta(self, n: int) -> int:
        if n == 1:
            return 1
        return n-1
    # ver alpha
    # we are not going to iterate a billion times
    # a hundred times is largely suffisant
    # then observe the result and try to find patterns
    def distinctIntegers(self, n: int) -> int:
        board = [n]
        for amuro in range(100):
            for x in board:
                for i in range(1,n+1):
                    if x % i == 1:
                        board.append(i)
                        board = list({key for key in board}) # delete duplicates
                        #             ^^^^^^^^^^^^^^^^^^^^^  this is not dict, it's a set
        print(board)
        return len(board)
epsi = Solution()
print(epsi.distinctIntegers(1))