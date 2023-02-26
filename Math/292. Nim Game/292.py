class Solution:
    # runtime 68.36%
    # memory 90.35%
    # i wonder how can i still optimize the runtime. Maybe there is a more efficient solution
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

# Explanation
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#  w  w  w  l  w  W  w  l  w  w   w   l   
# [1] At player X's turn, if there are 1 or 2 or 3 stones left, X can definitely win
# [2] At player X's turn, if there are 4 stones left, X will definitely lose
# [3] At my turn, if there are 5 stones left, if i take 1 stone, adversary will lose, so i can win. Ref [2]
# [4] The same for 6 or 7 stones left at my turn
# [5] At my turn, if there are 8 stones left, as i can only take 1 or 2 or 3 stones per turn, no matter how many stones i take, adversary can aways win
# [6] thus the distribution is : (win, win, win, lost, win, win, win, lost, win...)
# <=> Every three win, then one lost
# <=> i lost if initialy there are 4, 8, 12, 16 ... stones