class Solution:
    # ver alpha
    # firstly make an alpha version of O(n) time
    # then find the pattern and try to make a beta version
    def countOddsAlpha(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high+1):
            if i % 2 == 1:
                res -=- 1
        return res 
    # ver beta
    # pattern found : 
    # there are three cases, depending on the singularity of low and high
    # case 1 odd odd
    # case 2 even even
    # case 3 odd even / even odd
    # Different formula to calculate the result.
    # O(1)
    # runtime 27 ms 86.69%
    # memory 13.8 MB 48.97%
    def countOddsBeta(self, low: int, high: int) -> int:
        # if low and high is one odd one even
        if (low * high) % 2 == 0 and (low + high) % 2 == 1 :
            return int((high-low+1)/2)
        
        # then low and high have the same singularity
        
        # both odd
        if low % 2 == 1:
            return int((high-low+1)//2+1)
        # both even
        return int((high-low+1)//2)
epsi = Solution()


testcase = [(3,7), (3,6), (4,9), (2,10)]
testcaseOddOdd = [(3,7), (3,9), (1,9), (5,17)]
testcaseEvenEven = [(2,6), (2,8), (0,10), (6,16)]
testcaseOddEven = [(3,6), (3,8), (1,10), (7,16)]
#            ^ ^                          odd odd
#                   ^ ^                   odd even
#                         ^ ^             even odd
#                                 ^^  ^   even even

# testing
for case in testcaseOddEven:
    print("testcase : %s" % str(case))
    print("res : %s" % epsi.countOddsBeta(case[0], case[1]))
