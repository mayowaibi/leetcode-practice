class Solution:
    # Solution 1
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            maxProfit = max(maxProfit, price - lowest)

        return maxProfit

    # Solution 2: Sliding Window
    def maxProfit2(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit