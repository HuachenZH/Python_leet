class Solution:
    # ver alpha
    def differenceOfSum(self, nums: list[int]) -> int:
        elementSum = sum(nums)
        numsStr = [] # create an empty list, where digit sum of each number of nums  will be stored
        for num in nums:
            numsStr.append(sum(int(digit) for digit in [*str(num)]))
            #                                          ^^^^^^^^^^  = split every single character of the string and there will be a list
        print("numsStr is %s" % numsStr)
        digitSum = sum(numsStr)
        return abs(digitSum - elementSum)
epsi = Solution()
print(epsi.differenceOfSum([1,15,6,3]))

# to split every single character in a string, to methods to do so:
# word = "word"
# list(word)
# [*word]
