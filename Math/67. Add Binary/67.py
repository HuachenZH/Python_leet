class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = str(bin(int(a,2)+int(b,2)))[2:]
        return res

# The int() function takes as second argument the base of the number to be converted, which is 2 in case of binary numbers.
    
if __name__ == "__main__":
    epsilon = Solution()
    print(epsilon.addBinary("1","1"))
