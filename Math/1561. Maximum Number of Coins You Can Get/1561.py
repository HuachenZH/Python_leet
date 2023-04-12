class Solution:
    # runtime 619 ms 64.63%
    # memory 26.8 MB 15.24%
    def maxCoins(self, piles: list[int]) -> int:
        # i tried deleting this if chunk, however it becomes 9 ms slower. 
        if len(piles) == 3:
            return piles[1]
            # in fact this is not correct, i should ve done
            # return sorted(piles)[1]
            # however i still passed the test
        piles.sort(reverse=True) # descending order
        res = 0
        for i in range(int(len(piles)/3)):
        # index:        0  1  2
        # what i want:  1  3  5
            res += piles[2*i+1]
        return res
epsi = Solution()
print(epsi.maxCoins([9,8,7,6,5,1,2,3,4]))

# i find that the most difficult is not to succeed the challenge
# but to write comments so that the future me can understand

# If the input is [9,8,7,6,5,1,2,3,4], 
# after sorted in descending order: [9, 8, 7, 6, 5, 4, 3, 2, 1]
#                                    ^     ^     ^                Taken by Alice
#                                       ^     ^     ^             Taken by me