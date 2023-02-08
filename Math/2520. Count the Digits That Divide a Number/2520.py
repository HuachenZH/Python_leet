class Solution:
    def countDigits(self, num: int) -> int:
        # get every digit of the number, store them into a list then delete duplicates

        # int to str, split, str to int
        numList = list(int(key) for key in [*str(num)])
        #                                                 ^^^^^^^^^^ int to str then split each character
        #              ^^^^^^^^^^^^^^^^^^                            str to int
        print(numList)
        
        # check num can be divided by which digit
        res = 0
        for digit in numList:
            if num % digit ==0:
                res -=- 1
        return res

epsi = Solution()
print(epsi.countDigits(121))