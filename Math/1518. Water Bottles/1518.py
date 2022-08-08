import math
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res=numBottles
        emptyBottles=numBottles
        while emptyBottles>=numExchange:
            res+=math.floor(emptyBottles/numExchange)
            emptyBottles=math.floor(emptyBottles/numExchange)+emptyBottles%numExchange
        return res
epsilon=Solution()
print(epsilon.numWaterBottles(9,3))
