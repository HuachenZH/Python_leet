# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import math
class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n <= 3:
            for i in range(1,n+1):
                if isBadVersion(i):
                    return i 
        left = 1
        right = n
        while right - left > 2 :
            if isBadVersion(math.floor((left+right)/2)): # if middle version is bad
                right = math.floor((left+right)/2)
            else:
                left = math.floor((left+right)/2)
        for i in range(left, right+1):
            if isBadVersion(i):
                return i