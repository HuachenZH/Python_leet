class Solution:
    # solution with dictionary
    def romanToInt1(self, s: str) -> int:
        ref={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=0
        res+=ref[s[len(s)-1]] # the last roman numeral
        for i in range(len(s)-2,-1,-1): # the last roman numeral excluded
            if ref[s[i]] < ref[s[i+1]] :
                res-=ref[s[i]]
            else:
                res+=ref[s[i]]                
        return res

    # solution with map() (hint leetcode) --> not found :(
epsilon=Solution()
print(epsilon.romanToInt('III'))
