
class Solution:
    # ver alpha
    # i dont think it s necessary to create a matrix and do all the operations in ops
    # as there are matrix and vector stuffs, i used numpy
    # and not surprisely, the performance is not optimized according to leetcode
    # runtime 178 ms 5.7%
    # memory 34.3 MB 7.43%
    def maxCountAlpha(self, m: int, n: int, ops: list[list[int]]) -> int:
        # special case : no operation
        if len(ops) == 0:
            return m*n
        # else, in other cases 
        import numpy as np
        ops = np.array(ops)
        return ops.min(axis=0).prod()
    
    # ver beta
    # same approach as ver alpha but without numpy
    # performance :
    # runtime 64 ms 96.11%
    # memory 16 MB 22.80%
    def maxCountBeta(self, m: int, n: int, ops: list[list[int]]) -> int:
        # special case : no operation
        if len(ops) == 0:
            return m*n
        # else, in other cases
        # find the smallest of column without using numpy
        smallestCol0 = ops[0][0]
        smallestCol1 = ops[0][1]
        for row in ops:
            if row[0] < smallestCol0:
                smallestCol0 = row[0]
            if row[1] < smallestCol1:
                smallestCol1 = row[1]
        return smallestCol0 * smallestCol1
    # ver gamma
    # same approach as ver beta
    # the difference is, to find the smallest amongst each column
    # i use a list
    # performance :
    # runtime 71 ms 76.1%
    # memory 15.9 MB 70.27%
    # i m quite surprise that memory usage is more optimized than ver beta
    def maxCountGamma(self, m: int, n: int, ops: list[list[int]]) -> int:
        # special case : no operation
        if len(ops) == 0:
            return m*n
        # else, in other cases
        # find the smallest of column without using numpy
        col0 = []
        col1 = []
        for row in ops:
            col0.append(row[0])
            col1.append(row[1])
        return min(col0) * min(col1)

epsi = Solution()
print(epsi.maxCountBeta(3,3,[[20,10],[26,11],[2,11],[4,16],[2,3],[23,13],[7,15],[11,11],[25,13],[11,13],[13,11],[13,16],[26,17]]))

# after all, no matter how the performance tells
# i still prefer the numpy solution