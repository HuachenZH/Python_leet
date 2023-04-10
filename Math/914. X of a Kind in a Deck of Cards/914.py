class Solution:
    # runtime 140 ms 41.1%
    # memory 14.3 MB 60.71%
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        # iterate through the list, add their account to a dictionary,
        # where the key is the number itself,
        # the value is how many times the number appears.
        # Then iterate the dictionary to check if all the values are the same

        # as in most of the leet challenges, there are always extreme cases, like a trap.
        if len(deck) == 1:
            return False

        hashmap = {}
        for num in deck:
            # in python we can use the in keyword to check whether a key is in dict or not
            if num in hashmap:
                hashmap[num] += 1
            else: 
                hashmap[num] = 1
        
        # if a number appears only one times, then we already know it's False.
        # as said in the challenge statement, x > 1
        if 1 in hashmap.values():
            return False
        
        # check if all the values are the same
        # https://stackoverflow.com/questions/5073624/how-do-i-check-if-values-in-a-dictionary-all-have-the-same-value-x
        if len(set(hashmap.values())) == 1: 
            # all the values are the same
            return True
        # it returns True for cases like [1,2], [1,1,2,2]
        # however for cases like [1,2,2], [1,1,2,2,2,2], they are also true.

        # check the list of values. If the list of value is like {1,2}, {2,6}, {3,6,9}, then it shall be True.
        # if the list of value is like {2,3,6}, then it shall be False.
        # This means, check whether the smallest is the divisor of others.
        # -----
        # sorry the above statement is not totally correct, i havent covered cases like [1,1,1,1,2,2,2,2,2,2]
        # update: check whecther the list of value has a common divisor

        # in python, it's possible to sort a set
        val_list = sorted(set(hashmap.values()))
        # math.gcd() get common divisor function only takes two arguments, it does not suit for cases like
        # [2,2,4,4,4,4,6,6,6,6,6,6] which list of value is {2,4,6}
        for i in range(2,val_list[0]+1): # we will test if i is a divisor. So we can stop up to the smallest value
            flag = 0
            for val in val_list:
                if val % i == 0: # if i is a divisor:
                    flag += 1
            if flag == len(val_list):
                return True
        return False
        
epsi = Solution()
print(epsi.hasGroupsSizeX([1,1,2,2,2,2]))
