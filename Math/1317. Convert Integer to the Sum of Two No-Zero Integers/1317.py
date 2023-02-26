class Solution:
    # i tried to find a smart way but i failed
    # runtime 30 ms 79.49%
    # memory 13.8 MB 48.86%

    def zeroInInteger(self, n:int) -> bool:
        """
        return True if there is zero
        """
        return "0" in str(n)
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for i in range(1, n//2+1):
            if self.zeroInInteger(i)==False and self.zeroInInteger(n-i)==False:
                return [i, n-i]
        return -1

    # -------------------
    # i tried this, i thought i would be faster but not at all
    # runtime 37 ms 38.99%
    # memory 13.9 MB 8.10%
    def getNoZeroIntegers2(self, n: int) -> list[int]:
        for i in range(1, n):
            if "0" not in str(i) and "0" not in str(n-i):
                return [i, n-i]
        return -1
    # --------------------
    # here is the fastest solution
    def getNoZeroIntegers3(self, n: int) -> List[int]:
        for i in range(n-1,0,-1):
            if (not '0' in str(i)) and (not '0' in str(n-i)):
                return [i,n-i]
    # the difference is in the iteration, it starts from biggest to smallest.
    # i tested and it was truely bit faster


epsi = Solution()
testcase = [2, 3, 8, 9, 10, 11, 12, 53, 80, 1010]
for i in testcase:
    print("test case %s , result: %s" % (i,epsi.getNoZeroIntegers(i)))