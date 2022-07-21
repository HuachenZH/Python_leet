class Solution:
    def oneTo(self, n:int) -> int:
        if n==-1:
            return 0
        else:
            return n+self.oneTo(n-1)

    def totalMoney(self, n: int) -> int:
        res=self.oneTo(7)*int(n/7) + self.oneTo(int(n/7)-1)*7 + self.oneTo(n%7)+int(n/7)*(n%7)

        return res

sol=Solution()
print(sol.totalMoney(20))
    # 1                   1       2       3       4       5
    # 2                   2       3       4       5       6
    # 3                   3       4       5       6       7
    # 4                   4       5       6       7       8
    # 5                   5       6       7       8       9
    # 6                   6       7       8       9       10
    # 7                   7       8       9       10      11
    # 2                                                   
    # 3                   28      35      42      49      56
    # 4                           28      28      28      
    # 5                   0*7     1*7     2*7     3*7     
    # 6                                                   
    # 7                                                   
    # 8                                                   
    # 3       1   2                                       
    # 4       2   2                                       
    # 5       3   2                                       
                                                        
