class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(n-1):
            ans.append(i+3)
        ans.append(-1*sum(ans))
        return ans
# test passed, the performance is great, but this is absolutly not the expected code.
# There must be more elegant solutions

# ans.append(i+3)
# +3 because, without it, when n is 2, the output will be [0, 0] and is not correct
