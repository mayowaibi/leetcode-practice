class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res, empty = numBottles, numBottles

        while empty >= numExchange:
            newBottles = empty // numExchange
            res += newBottles
            empty = empty % numExchange
            empty += newBottles
        
        return res