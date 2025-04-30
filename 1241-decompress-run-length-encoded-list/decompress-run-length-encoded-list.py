class Solution:
    # Two Pointer Solution - TC: O(n), SC: O(1)
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        i, j = 0, 1
        while j < len(nums):
            freq, val = nums[i], nums[j]
            for _ in range(freq):
                res.append(val)
            i += 2
            j += 2
        
        return res