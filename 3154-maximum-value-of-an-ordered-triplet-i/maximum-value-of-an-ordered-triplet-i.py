class Solution:
    # Brute Force Greedy Solution - from 'value of triplet of indices' formula, we want to:
    # maximize nums[i], minimize nums[j] and maximize nums[k]
    # TC: O(n^2), SC: O(1)
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0

        left = nums[0]
        for j in range(1, len(nums)-1):
            if nums[j] > left:
                left = nums[j]
                continue
            for k in range(j + 1, len(nums)):
                res = max(res, (left - nums[j]) * nums[k])

        return res

    # Brute Force Solution - TC: O(n^3), SC: O(1)
    def maximumTripletValue2(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    res = max(res, (nums[i] - nums[j]) * nums[k])

        return res