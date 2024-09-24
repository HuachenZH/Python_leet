from math_2707 import Solution
import unittest

# dwmodizxvvbosxxw

class TestStringMethods(unittest.TestCase):

    #def test_upper_0(self):
    #    solution = Solution()
    #    self.assertEqual(solution.minExtraChar('dwmodizxvvbosxxw', ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]), 7)

    #def test_upper_1(self):
    #    solution = Solution()
    #    self.assertEqual(solution.minExtraChar('azvzulhlwxwobowijiyebeaskecvtjqwkmaqnvnaomaqnvf', ["na","i","edd","wobow","kecv","b","n","or","jj","zul","vk","yeb","qnfac","azv","grtjba","yswmjn","xowio","u","xi","pcmatm","maqnv"]), 15)
    
    def test_upper_2(self):
        solution = Solution()
        self.assertEqual(solution.minExtraChar('rkmsilizktprllwoimafyuqmeqrujxdzgp', ["afy","lyso","ymdt","uqm","cfybt","lwoim","hdzeg","th","rkmsi","d","e","tp","r","jx","tofxe","etjx","llqs","cpir","p","ncz","ofeyx","eqru","l","demij","tjky","jgodm","y","ernt","jfns","akjtl","wt","tk","zg","lxoi","kt"]), 2)



# Analysis
# dwm o diz x v v bosxxw
# ___ * *** _ * * ______
# output: 8, incorrect
# split at "o" so that i cannot split again at "wmo", and split at "wmo" is more optimized
# and notice, in this case i need to split "v" two times
# 
# d wmo diz x v v bosxxw
# _ *** *** _ * * ______  
# output: 7, correct

# imagine in "dictionary" you have "wmo" and "o"
# after splitting "wmo", you cannot split the "o" inside again

# maybe one word in "dictionary" has less length but more occurrence
# e.g. s="wawao" , word1="wa" and word2="wao". word1 is more optimal


# solution 3: sort dictionary by length of word
   

if __name__ == '__main__':
    unittest.main()


