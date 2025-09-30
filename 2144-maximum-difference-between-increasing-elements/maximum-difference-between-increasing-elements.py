class Solution:
    # TC: O(n), SC: O(1)
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        res = -1

        for i in range(1, len(nums)):
            if nums[i] > min_val:
                res = max(res, nums[i] - min_val)
            else:
                min_val = nums[i]
        
        return res