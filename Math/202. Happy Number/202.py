class Solution:
    # ver alpha
    # runtime 434 ms 5.25%
    # memory 13.8 MB 95.56%
    def isHappyAlpha(self, n: int) -> bool:
        actual = 0
        previous = n
        for i in range(1000):
            # get sum square of digits
            actual = sum(num**2 for num in [int(digit) for digit in str(previous)])
            # if sum square of digits is one, then previous is a happy number
            if actual == 1:
                return True
            # if not yet happy, continue
            previous = actual
        # print("it ends at i = %s" % i)
        return False
    
    # ver beta
    # put get sum square of digits into a function and check it s faster or not
    # nearly same performance as ver alpha
    # runtime 426 ms, 8 ms improved
    def getDigitSumSquare(self, previous: int) -> int:
        return sum(num**2 for num in [int(digit) for digit in str(previous)])
    def isHappyBeta(self, n: int) -> bool:
        actual = 0
        previous = n
        for i in range(1000):
            # get sum square of digits
            actual = self.getDigitSumSquare(previous)
            # if sum square of digits is one, then previous is a happy number
            if actual == 1:
                return True
            # if not yet happy, continue
            previous = actual
        # print("it ends at i = %s" % i)
        return False

    # ver gamma
    # try not using generator object, check faster or not
    # runtime much improved, 304 ms, 122 ms improvec
    # memory 13.9 MB, more 0.1 MB used, however it falls to 10.74%
    def getDigitSumSquare(self, previous: int) -> int:
        res = 0
        for digit in str(previous):
            res += int(digit)**2
        return res
    def isHappyGamma(self, n: int) -> bool:
        actual = 0
        previous = n
        for i in range(1000):
            # get sum square of digits
            actual = self.getDigitSumSquare(previous)
            # if sum square of digits is one, then previous is a happy number
            if actual == 1:
                return True
            # if not yet happy, continue
            previous = actual
        # print("it ends at i = %s" % i)
        return False
    
    # ver delta
    # less iteration
    # runtime 62 ms 9.82%
    # memory usage same as ver gamma
    def getDigitSumSquare(self, previous: int) -> int:
        res = 0
        for digit in str(previous):
            res += int(digit)**2
        return res
    def isHappyDelta(self, n: int) -> bool:
        actual = 0
        previous = n
        for i in range(100):
            # get sum square of digits
            actual = self.getDigitSumSquare(previous)
            # if sum square of digits is one, then previous is a happy number
            if actual == 1:
                return True
            # if not yet happy, continue
            previous = actual
        # print("it ends at i = %s" % i)
        return False


    # the problem is not about number of iteration, but about my approach
    # here is the approach of fastest solution on leetcode, coded in my ver
    # ver zeta
    # use set
    def isHappy(self, n: int) -> bool:
        seen = set()
        # we start to iterate. 
        while n not in seen:
        # if the new n is not in the set seen, do the iteration
        # if the new n is already in the set seen, it means the actual n and the previous n have the same value
            nextt = 0
            seen.add(n) # add the actual n to the set
            
            # get digit sum square. Pure math approach
            while n: 
            # when n is no zero, it equals to True
            # when n is zero, it equals to False
                nextt += (n%10)**2
                n //= 10
            # if the digit sum square equals to one, then the number is happy, no need to continue the iteration
            if nextt == 1:
                return True
            # else, in this iteration we cannot prove the number is happy, so take to next iteration
            n = nextt # restore the value of n, as it is changed while computing the digit sum square
        return False
epsi = Solution()
print(epsi.isHappy(2))
