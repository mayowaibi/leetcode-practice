class Solution:
    # One-line Solution w/ List Comprehension - TC: O(n), SC: O(1)
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[num] for num in nums]