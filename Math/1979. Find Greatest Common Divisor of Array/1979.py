import math
class Solution:
    def findGCD(self, nums: list[int]) -> int:
        return math.gcd(min(nums),max(nums))
sol=Solution()
print(sol.findGCD([3,3]))
