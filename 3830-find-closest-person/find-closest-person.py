class Solution:
    # Easiest LeetCode question I've ever seen
    # Constant time complexity???
    # TC: O(1), SC: O(1)
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist1 = abs(z-x)
        dist2 = abs(z-y)

        if dist1 < dist2:
            return 1
        elif dist2 < dist1:
            return 2
        else:
            return 0