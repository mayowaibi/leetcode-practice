class Solution:
    # Two Pointer Solution - TC: O(n), SC: O(1)
    def applyOperations(self, nums: List[int]) -> List[int]:
        # apply operations
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        # move 0s to end
        l = 0   # keeps track of first available slot for a swap (0s)
        for r in range(len(nums)):
            # swap r with first available slot if non-zero
            # then increment l only when a swap occurs
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            
        return nums