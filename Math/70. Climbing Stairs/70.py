class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 step : 1 way
        # 2 step : 2 way
        # 3 step : 2+1=3 way
        # 4 step : 2+3=5 way
        # s(n) = s(n-1) + s(n-2)
        if n==1:
        	return 1
        if n==2:
        	return 2
        minus1=1
        minus2=2
        for i in range(n-2):
        	res = minus1 + minus2
        	minus1 = minus2
        	minus2 = res
        return res

if __name__ == "__main__":
    epsilon = Solution()
    print(epsilon.climbStairs(5))

