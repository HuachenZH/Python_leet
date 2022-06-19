class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        # it's all about parity, even or odd. 
        # when the parity is not changed, the cost is 0. When the parity is changed, the cost is 1.
        # in example 3, from 1 to 100000, 1 to 2, then 2 to 100000, the parity changes only one time, so the cost is only 1.
        # which is the final number, is not at all important, since there is no cost when 1->3->5->7...etc.

        # if input is [2,2,2,3,3], the majority is even, so we need to transform 3,3 to 2,2, the parity changes two times, so the cost is 2.
        # if input is [1,2,3], the majority is odd, so we need to do 2->1or3. The parity changes one time, the cost is 1.

        # Approach:
        # 1. find which is the majority, even or odd
        # 2. then find the count of minority

        # Approach improved:
        # 1. find the count of minority, this will be the cost.
        countOdd=0
        countEven=0
        for i in position:
            if i%2==0: # even
                countEven+=1
            else: # odd
                countOdd+=1
        return min(countOdd,countEven)

sol=Solution()
print(sol.minCostToMoveChips([1,1000000]))

