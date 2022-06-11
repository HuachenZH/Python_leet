class Solution:
    def maximum69Number (self, num: int) -> int:
        # a pure maths approach
        for i in range(len(str(num))-1,-1,-1): # decrementing with range.
            if int(num/10**i%10)==6:
                num+=3*10**i
                break
        return num
            




sol=Solution()
print(sol.maximum69Number(9669))
