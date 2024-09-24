import pdb

class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        # sort "dictionary" by length of its words, descending order
        dictionary.sort(key=len, reverse=True)
        for word in dictionary:
            if word in s: # this if chunk is just for debugging
                s = s.replace(word, "_"*len(word))
                # breakpoint()
                print(word)
                print(s)
        return len(s)




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