class Solution:
    # runtime could be better. 
    # runtime 47.26%
    # memory 63.35%
    def divisibleString(self, str1: str, str2: str) -> bool:
        '''
        Check if the str1 % str2 == 0. 
    
            Parameters
            ----------
            str1 : str
                The bigger string.
            str2 : str
                The smaller string
    
            Returns
            -------
            bool
                Return True if str1 % str2 == 0. False if str1 % str2 != 0
    
        '''
        if len(str1) % len(str2) != 0:
            return False
        compare = ''
        for i in range(int(len(str1)/len(str2))):
        # len(str1)/len(str2) is float. So i put int() to convert to int
            compare += str2
        return compare == str1
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if their lengths are equal, then only need to test if str1 % str2 == 0
        if len(str1) == len(str2):
            if self.divisibleString(str1, str2):
                return str1
            return ""
        # convention: str1 is the larger, str2 is the smaller
        if len(str1)<len(str2):
            tmp = str2
            str2 = str1
            str1 = tmp
            del tmp
        # new str1 is the larger, str2 is the smaller

        # in order to be a gcd, it must be a factor of the smaller string, then a factor of the larger string
        for i in range(len(str2)-1,-1,-1):
            # test if str2[0:i] is a commun factor
            # print(str2[0:i+1])
            # print(i)
            # firstly it must be a factor of the smaller stirng
            if self.divisibleString(str2, str2[0:i+1]):
                # check for the larger string
                if self.divisibleString(str1, str2[0:i+1]):
                    return str2[0:i+1]
        return ""
epsi = Solution()
print(epsi.divisibleString("ABCABC", "ABC"))
epsi.gcdOfStrings("ABCABC", "ABC")

testCases = [("ABCABC", "ABC"), ("ABCABC", "AB"), ("ABCDEF","ABC")]
for testCase in testCases:
    print("Test case: %s %s" % (testCase[0], testCase[1]))
    print("- divisableString : %s" % epsi.divisibleString(testCase[0], testCase[1]))
    print("- gcdOfStrings : %s" % epsi.gcdOfStrings(testCase[0], testCase[1]))
    print("")