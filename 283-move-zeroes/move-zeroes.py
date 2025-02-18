class Solution:
    # Two-Pointer Solution - TC: O(n), SC: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0  # represents the index for the next non-zero number to move to

        for right in range(len(nums)):
            # swap non-zero nums from right index
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1   # only increment left when a swap occurs