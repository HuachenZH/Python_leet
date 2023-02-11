class Solution:
    def isPalindromic(self, n: int) -> bool:
        return str(n) == str(n)[::-1]
    def isStrictlyPalindromic(self, n: int) -> bool:
        # from base 2 to base n-2
        for b in range(2, n-1):
            # representation of integer n in base b
            # convert to base b
            ninb = []
            n_tmp = n
            while n_tmp > 0:
                ninb.insert(0,str(n_tmp%b)) # add to the start of list. Like unshift in js
                # so that the digits are in the correct order while doing string.join() later
                # as the goal is only to check palindromic or not, it's the same thing with .append()
                n_tmp = n_tmp //b
            print(ninb)
            # if in base b, not palindromic, return false
            if not self.isPalindromic("".join(ninb)):
                return False
        # otherwise, after iterating through all bases, it must be strictly palindromic
        return True
epsi = Solution()
print(epsi.isStrictlyPalindromic(9))

# cf 1837 for base changes