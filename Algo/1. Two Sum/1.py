class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return '404'
    
    # solution of leet: one-pass hashmap
    # add elements of the list nums into a dictionary as key, their index as value
    # while adding, check if the complementry already exists in the dictionary
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        dictionary={}
        for i in range(len(nums)):
            if target-nums[i] in dictionary:
                return [i, dictionary[target-nums[i]]]
            dictionary[nums[i]]=i
    # we add nums[i] into the dictionary after check if, to avoid the situation that nums[i]+nums[i]==target

epsilon=Solution()
print(epsilon.twoSum2([2,7,11,15],9))