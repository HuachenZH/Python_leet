class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # A pair (i, j) is called good if nums[i] == nums[j] and i < j.
        
        # first for loop : i
        for i in range(len(nums)-1):
            # second for loop : j
            for j in range(1,len(nums)):
                print(i,j)
        return "finish"
sol=Solution()
sol.numIdenticalPairs([1,2,3,1,1,3])
