class Solution:
    # TC: O(n), SC: O(1)
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = empty = 0

        while numBottles > 0:
            # drink bottles
            res += numBottles
            empty += numBottles
            numBottles = 0

            # continue exchanging empty bottles if possible
            # and increment numExchange each time
            while empty >= numExchange:
                empty -= numExchange
                numBottles += 1
                numExchange += 1
        
        return res