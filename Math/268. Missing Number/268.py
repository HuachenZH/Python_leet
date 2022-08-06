class Solution:
    def termial(self,num:int) -> int:
        res=0
        for i in range(num+1):
            res+=i
        return res
    def missingNumber(self, nums: list[int]) -> int:
        return self.termial(len(nums))-sum(nums)
    
epsilon=Solution()
print(epsilon.missingNumber([9,6,4,2,3,5,7,0,1]))

