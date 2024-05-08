class Solution:
    # Mathematical Formula Solution - TC: O(1), SC: O(1)
    def arrangeCoins(self, n: int) -> int:
        return int(sqrt(2 * n + 0.25) - 0.50)