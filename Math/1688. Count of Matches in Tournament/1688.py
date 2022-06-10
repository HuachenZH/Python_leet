class Solution:
    def numberOfMatches(self, n: int) -> int:
        res=0 # matches played
        while n!=1:  # the value of n will change. It's the remaining team.
            if n%2==1: # when n is odd
                res+=(n-1)/2
                n=(n+1)/2 # for example, 7 --> 4
            else: # when n is even
                res+=n/2
                n/=2
        return int(res)
sol=Solution()
print(sol.numberOfMatches(14))
