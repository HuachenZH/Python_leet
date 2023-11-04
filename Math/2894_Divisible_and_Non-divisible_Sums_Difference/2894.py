class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(1, n+1):
            # not divisible
            if i % m != 0:
                num1 += i
            # divisible
            else:
                num2 += i
        return num1 - num2
    
    def test(self):
        """test function"""
        print(self.differenceOfSums(10, 3))
        print(self.differenceOfSums(5, 6))
        print(self.differenceOfSums(5, 1))

epsilon = Solution()
print(epsilon.test())