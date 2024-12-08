class Solution:
    # TC: O(n), SC: O(1)
    # Seconds between two points = max diff b/w their x or y coords
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0

        for i in range(1, len(points)):
            prev_x, prev_y = points[i-1][0], points[i-1][1]
            x, y = points[i][0], points[i][1]
            
            res += max(abs(x - prev_x), abs(y - prev_y))

        return res