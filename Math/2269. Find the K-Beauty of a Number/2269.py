class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res=0
        tmp=0
        for i in range(len(str(num))-k+1):
            tmp=int(str(num)[i:i+k])
            if tmp==0:
                continue
            else:
                if num%tmp==0:
                    res+=1
        return res
epsilon=Solution()
print(epsilon.divisorSubstrings(430043,2))
