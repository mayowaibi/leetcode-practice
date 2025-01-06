class Solution:
    # Brute Force Solution - TC: O(n^2), SC: O(1)
    def finalPrices(self, prices: List[int]) -> List[int]:

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break

        return prices