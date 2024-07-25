class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        minimum = min(nums)
        smallest_diff = (maximum-k) - (minimum+k)

        return max(0, smallest_diff)