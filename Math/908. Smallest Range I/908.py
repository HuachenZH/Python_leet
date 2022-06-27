class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums=np.array(nums)
		
        return np.average(nums)
sol=Solution()
print(sol.smallestRangeI([1,10,5,40],20))
