import math
class Solution:
    # ver beta
    # without list, without math. Will it be faster ?
    # a bit slower comparing to ver alpha but memory is much more optimized
    # runtime 94.10%
    # memory 88.10%
    def averageValueBeta(self, nums: list[int]) -> int:
        summ = 0
        count = 0
        for num in nums:
            if num % 6 == 0:
                summ += num
                count -=- 1
        if count == 0:
            return 0
        return summ//count

    # ver alpha
    # with list, math
    # runtime 98.11%
    # memory 17.24%
    def averageValueAlpha(self, nums: list[int]) -> int:
        # even integers that are divisible by 3
        # that means integers divisible by 6
        oklist = []
        for num in nums:
            if num % 6 == 0:
                oklist.append(num)
        if len(oklist)==0:
            return 0
        print(sum(oklist)/len(oklist))
        return math.floor(sum(oklist)/len(oklist))
epsi = Solution()
print(epsi.averageValueAlpha([43,9,75,76,25,96,46,85,19,29,88,2,5,24,60,26,76,24,96,82,97,97,72,35,21,77,82,30,94,55,76,94,51]))