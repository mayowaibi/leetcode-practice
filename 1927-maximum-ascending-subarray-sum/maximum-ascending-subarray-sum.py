class Solution:
    # Optimized Solution - TC: O(n), SC: O(1)
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = curr = nums[0]

        for i in range(1, len(nums)):
            if not (nums[i-1] < nums[i]):
                curr = 0
            curr += nums[i]
            res = max(res, curr)

        return res

    # Brute-Force Solution - TC: O(n^2), SC: O(1)
    def maxAscendingSum2(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] > nums[j-1]:
                    curr += nums[j]
                    res = max(res, curr)
                else:
                    break

        return res