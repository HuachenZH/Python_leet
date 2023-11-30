# solution 1: with a list
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # A pair (i, j) is called good if nums[i] == nums[j] and i < j.
        outList=list()
        # first for loop : i
        for i in range(len(nums)-1):
            # second for loop : j
            for j in range(i+1,len(nums)):
                # now we already fulfil the condition i<j
                # let's check if nums[i] == nums[j] 
                if nums[i] == nums[j]:
                    # add the pair i,j into a list as tuple
                    outList.append((i,j))
        print(outList)
        return len(outList)
sol=Solution()
sol.numIdenticalPairs([1,1,1,1])



# solution 2 : no list, just count
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # A pair (i, j) is called good if nums[i] == nums[j] and i < j.
        count=0
        # first for loop : i
        for i in range(len(nums)-1):
            # second for loop : j
            for j in range(i+1,len(nums)):
                # now we already fulfil the condition i<j
                # let's check if nums[i] == nums[j] 
                if nums[i] == nums[j]:
                    count=count+1
        return count
