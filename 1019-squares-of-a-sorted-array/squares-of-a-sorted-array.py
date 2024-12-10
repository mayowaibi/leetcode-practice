class Solution:
    # Two (Technically Three) Pointer Solution - TC: O(n), SC: O(1) assuming output arr doesn't count
    # Solution works by first filling res arr in inc. order with l+r pointer comparisons
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l, r = 0, len(nums) - 1
        i = len(nums) - 1   # to keep track of where to add the current num

        while l <= r and i >= 0:
            l_squared, r_squared = nums[l]**2, nums[r]**2

            if l_squared >= r_squared:
                res[i] = l_squared
                l += 1
            elif r_squared > l_squared:
                res[i] = r_squared
                r -= 1
            i -= 1

        return res

    # Sorting Solution - TC: O(nlogn), SC: O(1)
    def sortedSquares2(self, nums: List[int]) -> List[int]:

        res = [num ** 2 for num in nums]
        res.sort()

        return res