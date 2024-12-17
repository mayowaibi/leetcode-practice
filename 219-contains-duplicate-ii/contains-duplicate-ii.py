class Solution:
    # Sliding Window Solution - TC: O(n), SC: O(k)
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0

        for r in range(len(nums)):
            # resize window if larger than k
            if len(window) > k:
                window.remove(nums[l])
                l += 1
            # return True if duplicate is found in window
            if nums[r] in window:
                return True
            # add num to window if new
            window.add(nums[r])
        
        return False
            