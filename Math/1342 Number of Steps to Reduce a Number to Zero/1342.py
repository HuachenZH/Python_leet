class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num!=0:
            print(num)
            if num%2==0: # num is even
                num=num/2
            if num%2==1: # num is odd
                num-=1 # this version is not correct. 
            count+=1

        return count


sol=Solution()
print(sol.numberOfSteps(14))
