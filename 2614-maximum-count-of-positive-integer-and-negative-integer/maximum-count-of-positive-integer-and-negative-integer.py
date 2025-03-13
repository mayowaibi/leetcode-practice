class Solution:
    # Binary Search Solution - TC: O(logn), SC: O(1)
    def maximumCount(self, nums: List[int]) -> int:
        # find the first positive number (if any)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= 0:
                l = mid + 1
            elif nums[mid] > 0:
                r = mid - 1
        # at the end, l points to the first positive number
        pos = len(nums) - l

        # find the last negative number (if any)
        l, r  = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= 0:
                r = mid - 1
            elif nums[mid] < 0:
                l = mid + 1
        # at the end, r points to the last negative number
        neg = r + 1

        # return the larger value
        return max(pos, neg)


    # Basic Array Traversal - TC: O(n), SC: O(1)
    def maximumCount2(self, nums: List[int]) -> int:
        pos = neg = 0

        for n in nums:
            if n > 0:
                pos += 1
            if n < 0:
                neg += 1
        
        return max(pos, neg)