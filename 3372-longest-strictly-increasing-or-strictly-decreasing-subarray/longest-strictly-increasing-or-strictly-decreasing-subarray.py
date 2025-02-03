class Solution:
    # TC: O(n), SC: O(1)
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        incCount = decCount = 1

        for i in range(len(nums)-1):
            # strictly increasing
            if nums[i] < nums[i+1]:
                incCount += 1
                decCount = 1
            # strictly decreasing
            elif nums[i] > nums[i+1]:
                decCount += 1
                incCount = 1
            # equal
            else:
                incCount = decCount = 1
            
            res = max(res, incCount, decCount)

        return res