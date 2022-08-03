class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
        	return False
        else:
        	return int(str(x)[::-1])==x
epsilon=Solution()
print(epsilon.isPalindrome(123456654321))