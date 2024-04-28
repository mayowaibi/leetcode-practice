class Solution:
    # Using Helper Functions - TC: O(n), SC: O(1)
    def isMonotonic(self, nums: List[int]) -> bool:
        return self.isIncreasing(nums) or self.isDecreasing(nums)

    def isIncreasing(self, nums) -> bool:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return False
        return True

    def isDecreasing(self, nums) -> bool:
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                return False
        return True

    # Sorting and Comparing - TC: O(nlogn) SC: O(1)
    def isMonotonic1(self, nums: List[int]) -> bool:
        return nums == sorted(nums) or nums == sorted(nums, reverse = True)