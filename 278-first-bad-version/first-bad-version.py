# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # Binary Search Solution - TC: O(logn), SC: O(1)
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            version = left + (right - left) // 2

            if isBadVersion(version):
                right = version - 1
            else:
                left = version + 1

        return left