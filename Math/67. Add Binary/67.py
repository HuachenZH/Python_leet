class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = str(bin(int(a,2)+int(b,2)))[2:]
        return res

if __name__ == "__main__":
    epsilon = Solution()
    print(epsilon.addBinary("1","1"))
