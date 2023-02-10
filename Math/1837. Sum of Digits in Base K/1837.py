class Solution:
    def sumBase(self, n: int, k: int) -> int:
        listres = []
        while n > 0:
            listres.append(n%k)
            n = n //k
        print(listres)
        return sum(listres)
epsi = Solution()
print(epsi.sumBase(34,6))
