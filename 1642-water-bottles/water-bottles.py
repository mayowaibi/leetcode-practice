class Solution:
    # TC: O(logn) base e, SC: O(1)
    # where n = numBottles and e = numExchange
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = empty = 0

        while numBottles > 0:
            # drink bottles
            res += numBottles
            empty += numBottles
            numBottles = 0  # redundant but left for the sake of understanding

            # exchange empty bottles
            numBottles = empty // numExchange
            empty %= numExchange

        return res