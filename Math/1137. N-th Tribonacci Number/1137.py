class Solution:
    # # solution 1: recursive, time limit exceeded
    # def tribonacci(self, n: int) -> int:
    #     if n>2:
    #         return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
    #     if n==0:
    #         return 0
    #     else:
    #         return 1
    def tribonacci(self, n: int) -> int:
        tribo=[0,1,1]
        if n<3:
            return tribo[n]
        for i in range(n-2):
            tribo.append(tribo[len(tribo)-1]+tribo[len(tribo)-2]+tribo[len(tribo)-3])
        return tribo[n]
epsilon=Solution()
print(epsilon.tribonacci(25))

# i made error at line 5:
# return n+self.tribonacci(n-1)+self.tribonacci(n-2)
