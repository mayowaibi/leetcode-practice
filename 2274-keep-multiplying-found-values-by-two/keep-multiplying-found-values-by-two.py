class Solution:
    # TC: O(n), SC: O(n)
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2

        return original
