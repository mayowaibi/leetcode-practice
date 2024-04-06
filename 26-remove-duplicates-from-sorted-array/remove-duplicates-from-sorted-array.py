class Solution:
    # Two-Pointer Solution - TC: O(n), SC: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        # no need to start any pointer at 0 because first index is guaranteed to be unique
        # left pointer keeps track of unique values AND is used to replace duplicates
        l = 1

        for r in range(1, len(nums)):
            # if a new unique value is found
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        return l