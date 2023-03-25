class Solution:
    # Runtime 37 ms 43.58%
    # memory 13.9 MB 6.63%
    # pure for loop approach
    def plusOneAlpha(self, digits: list[int]) -> list[int]:
        # iterate the list from right to left (from least to most significant digit)
        for i in range(len(digits)-1,-1,-1):
            digits[i] -=- 1 # plus one to this digit
            if digits[i] != 10: # if it s under 10, return, no need to proceed to the next iteration
                return digits
            else:
                digits[i] = 0 # if it s 10, we cannot leave 10 at its place, so replace by 0, proceed to the next iteration because we need to plus one to the next digit
        if digits[0] == 0: # after the iteration, check if it s cases like 9, 99, 999... where another digit should be created
            digits.insert(0,1)
        return digits
    
    # runtime 31 ms 80.69%
    # memory 13.9 MB 47.54%
    # make digits a normal number
    # we won t use str here, it will loop through digits too many times
    def plusOneBeta(self, digits: list[int]) -> list[int]:
        num = 0
        # iterate throuth digits, take every digit and make them a true number
        for i in range(len(digits)):
            num += digits[i] * 10**(len(digits)-1-i)
        # plus one
        num += 1
        # split the int into a list of int
        res = []
        while num > 0:
            res.insert(0,num%10) # as most significant digit is on the left, we cannot use append here
            num //= 10
        return res

epsi = Solution()
print(epsi.plusOneBeta([4,3,2,1]))
