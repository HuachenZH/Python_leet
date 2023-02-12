class Solution:
    def minOperations(self, n: int) -> int:
        # two cases, n pair or n impair
        if n % 2 == 0: # n is pair
            t = (2*(n/2-1)+1 + 2*(n/2)+1)/2
            #    ^^^^^^^^^^^                 arr[n/2-1]
            #                  ^^^^^^^^^     arr[n/2]
            out = n/2*t - n*(1+2*(n/2-1)+1)/4
        else: # n is impair
            m = (n-1)/2
            out = (m+1)*(2*m+1) - (m+1)*(1+(2*m+1))/2
            #            ^^^^^^             ^^^^^^  arr[m]
        return int(out) 
epsi = Solution()
print(epsi.minOperations(5))

