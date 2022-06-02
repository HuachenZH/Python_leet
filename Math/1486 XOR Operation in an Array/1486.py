class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        for i in range(n):
            nums.append(start+2*i)
        res=nums[0]
        print(nums)
        for i in range(1,len(nums)):
        	res=res^nums[i]
        	print(res)
        return res

sol=Solution()
print(sol.xorOperation(4,3))
