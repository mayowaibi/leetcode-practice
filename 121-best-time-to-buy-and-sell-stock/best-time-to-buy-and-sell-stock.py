class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        # l is the buying day, r is the selling day
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            maxProfit = max(maxProfit, price - lowest)
        return maxProfit