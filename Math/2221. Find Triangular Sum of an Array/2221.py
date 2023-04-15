class Solution:
    # runtime 2622 ms 57.40%
    # memory 14.1 MB 39.25%
    # i checked the fastest solution but i dont understand what is it doing  TAT
    def triangularSum(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        while len(nums) > 1:
            newNums = []
            # iterate through the old array, calculate new value, then append the value to the new list
            for i in range(len(nums)-1):
                newNums.append((nums[i]+nums[i+1])%10)
            # replace the old array by the new array
            nums = newNums
        return nums[0]
    
epsi = Solution()
print(epsi.triangularSum([5]))
