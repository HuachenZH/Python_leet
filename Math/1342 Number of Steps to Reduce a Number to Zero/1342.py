class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num!=0:
            print(num)
            if num%2==0: # num is even
                num=num/2
            else: # num is odd
                num-=1
            count+=1

        return count


sol=Solution()
print(sol.numberOfSteps(14))
