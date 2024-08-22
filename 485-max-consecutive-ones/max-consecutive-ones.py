class Solution:
    # TC: O(n), SC: O(1)
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currMax, res = 0, 0

        for num in nums:
            if num == 1:
                currMax += 1
                res = max(res, currMax)
            else:
                currMax = 0

        return res