# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import math
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while right - left > 1 :
            if isBadVersion(math.floor((left+right)/2)): # if middle version is bad
                right = math.floor((left+right)/2)
            else:
                left = math.floor((left+right)/2)
        # after while loop, it remains three versions: k, k+1
        for i in range(left, right+1):
            if isBadVersion(i):
                return i