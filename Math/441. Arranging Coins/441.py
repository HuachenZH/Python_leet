class Solution:
    # runtime 36 ms 83.19%
    # memory 13.7 MB 93.76%
    def arrangeCoins(self, n: int) -> int:
        k = (((1+8*n)**0.5)-1)/2
        return int(k//1)

epsi = Solution()
print(epsi.arrangeCoins(5))

# explanation
# suppose we have k rows, 1, 2, 3 ... k-1, k. And the sum is n
# with the sum of sequence formula
# the relation between k and n is:
# (1+k)*k/2 = n
# in this equation, in our case, k is the unknown, n is known
# so we have k = (((1+8*n)**0.5)-1)/2
# in real case, the last row might be incompleted, that means, instead of k = 3 for a completed case, k might eqauls to 2.79455... for an incomplete case
# so we need to math.floor(k)
# to avoid importing math, i use int(k//1)