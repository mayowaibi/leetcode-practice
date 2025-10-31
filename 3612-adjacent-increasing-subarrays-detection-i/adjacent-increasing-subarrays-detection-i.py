class Solution:
    # TC: O(n), SC: O(1)
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        counter = k - 1

        if counter == 0: return True

        for i in range(k + 1, len(nums)):
            if nums[i] > nums[i - 1] and nums[i - k] > nums[i - k - 1]:
                counter -= 1
                if counter == 0:
                    return True
            else:
                counter = k - 1

        return False