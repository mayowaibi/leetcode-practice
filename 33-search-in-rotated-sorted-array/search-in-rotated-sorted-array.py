class Solution:
    # Binary Search Solution - TC: O(logn), SC: O(1)
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
        
            # left-sorted portion
            if nums[left] <= nums[mid]:
                # if target is between left and mid, search only left-sorted portion
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # else, search right-sorted portion
                else:
                    left = mid + 1
            # right-sorted portion
            if nums[right] >= nums[mid]:
                # if target is between mid and right, search only right-sorted portion
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # else, search left-sorted portion
                else:
                    right = mid - 1
        return -1

    # Linear Search Solution - TC: O(n), SC: O(1)
    def search2(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if n == target:
                return i

        return -1