class Solution:
    # Two Pointer Solution - TC: O(n), SC: O(1)
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        res = 0

        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                # Technically don't need to account for non-negative 
                # values being appended to res (no need for max check)
                res += max(0, max_left - height[l])
            else:
                r -= 1
                max_right = max(max_right, height[r])
                res += max(0, max_right - height[r])
        
        return res

    # Prefix + Suffix Arrays Solution - TC: O(n), SC: O(n)
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        max_left, max_right = [0] * n, [0] * n

        # Initialize every max_left[i] with 
        # the max val to the left of max_left[i]
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])

        # Initalize every max_right[i] with
        # the max val to the right of max_right[i]
        max_right[-1] = height[-1]
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])
        
        res = 0
        # Height of rain water = min(max_left[i], max_right[i]) - height[i]
        # Add the height of the rain water at each index to res using
        # the min of max_left[i] and max_right[i] as the bottleneck
        for i in range(n):
            res += max(0, min(max_left[i], max_right[i]) - height[i])

        return res