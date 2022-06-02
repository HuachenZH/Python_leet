class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        for i in range(n):
            nums.append(2*i)
        res=0
        for i in nums:
        	res=res^i

        return res
