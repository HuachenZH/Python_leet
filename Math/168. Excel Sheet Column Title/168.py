class Solution:
    # runtime 30 ms 67.42%
    # memory 13.8 MB 93.85%
    def num2letter(self, num: int) -> str:
        """Given a number, give its corresponding letter.
           num: from 1 to 26 (inclusive)
           A is 1, B is 2, C is 3... Y is 25, Z is 26"""
        if num == 0:
            return "Z"
        return chr(num + 64)
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber > 0:
            if columnNumber % 26 == 0: # columnNumber > 1, so if its modulo 26 is zero, then it must be 26's multiple
                res = "Z" + res # if it's 26's multiple, then the letter must be Z
                columnNumber -= 26 # this is the essential. 
                # for example if columnNumber = 52 (AZ)
                # with 52 % 26 = 0, we can find the rightmost letter is Z. That's correct
                # then 52 // 26 = 2. We will find the next letter is B. That's not correct
            else:
                # if it is not multiple of 26
                res = self.num2letter(columnNumber % 26) + res # find the corresponding letter and concat to the left of res
            columnNumber //= 26
        return res

epsi = Solution()


import unittest
class TestStringMethods(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(epsi.convertToTitle(722), 'AAT', msg="failed")
        self.assertEqual(epsi.convertToTitle(701), 'ZY', msg="failed")
        self.assertEqual(epsi.convertToTitle(26), 'Z', msg="failed at 26 - Z")
        self.assertEqual(epsi.convertToTitle(52), 'AZ', msg="failed at 52 - AZ")
        self.assertEqual(epsi.convertToTitle(1353), 'AZA', msg="failed")
        # AZ and AZA are the best examples to understand the algo.
if __name__ == '__main__':
    unittest.main()

# print(epsi.convertToTitle(722)) # AAT
# print(' ')
# print(epsi.convertToTitle(701)) # ZY

# i took a few time to find the solution. I will explain my approach below

# This goal is, given an int, give the column. 
# it seems difficult, so let's start by a simpler question : given a column, find the number.

# Column -> number
# Given JK, how to find the number ?
# J is 10th alphabet and K is the 11th.
# As on the "10's digit", it is J. It means, it has been iterating 26 letters for 10 times.
# On the "1's digit", it is K. It means, it's the 11th
# so we have 26 * 10 + 11 = 271, and 271 is the correct answer.

# Number -> column.
# Now let's reverse the problem. Given the number 271, how to find out "JK" as answer ?
# 271 % 26 = 11, K
# 271 // 26= 10, J
# what we found by % is on the 1's digit, what we found by // is on the 10's digit.

# But this is still a simple case, JK has only two letters.
# What about columns like AAT which has three letters ?
# Given that the number is 722, how to find AAT ?
# 722 % 26 = 20, T, on the 1's digit
# 722 //26 = 27. How to deal with 27?
    # 27 % 26 = 1, A (the A of the middle)
    # 27 //26 = 1, A (the A of the left)

# algo need to be restructured, totally