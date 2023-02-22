import math
class Solution:
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
        return
epsi = Solution()
print(epsi.divisibleString("ABCABC", "ABC"))
epsi.gcdOfStrings("ABCABC", "ABC")

testCases = [("ABCABC", "ABC"), ("ABCABC", "AB")]
for testCase in testCases:
    print("Test case: %s %s" % (testCase[0], testCase[1]))
    print("- divisableString : %s" % epsi.divisibleString(testCase[0], testCase[1]))
    print("")