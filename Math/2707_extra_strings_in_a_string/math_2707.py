class Solution:
    def minExtraChar_dep2(self, s: str, dictionary: list[str]) -> int:
        res = len(s)
        for word in dictionary:
            if word in s:
                res = res - len(word)
        return res
    


    def minExtraChar_dep1(self, s: str, dictionary: list[str]) -> int:
        for word in dictionary:
            s = s.replace(word, "")
        return len(s)