class Solution:

    def reverseInt(self, num: int) -> int:
        # reverse the integer by using string approach
        return int(str(num)[::-1])

    # runtime 799 ms 32.63%
    # memory 39.7 MB 58.39%
    # i'm not sure which approach will be faster for the reverseInt function, string approach or pure numeric approach.
    def countDistinctIntegersBeta(self, nums: list[int]) -> int:
        # the simplest approach, just do what it asks

        # iterate through the original list, reverse the integer then append to the end
        for i in range(len(nums)):
            nums.append(self.reverseInt(nums[i]))
        # delete duplicates in the list by using set
        nums_distinct = list({num for num in nums})
        return len(nums_distinct)
    
epsi = Solution()
print(epsi.reverseInt(256))
print(epsi.countDistinctIntegers([1,13,10,12,31]))
print(epsi.countDistinctIntegers([2,2,2]))
