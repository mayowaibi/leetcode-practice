class Solution:
    # Two Pointer Solution - TC: O(n), SC: O(1)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        product = 1

        l = 0
        for r in range(len(nums)):
            product *= nums[r]
            # while product >= k, keep removing value at left index
            # from product and incrementing left pointer
            while l <= r and product >= k:
                product = product // nums[l]
                l += 1
            # add difference between indices to result
            result += r - l + 1

        return result