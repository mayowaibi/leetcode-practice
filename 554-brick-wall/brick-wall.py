class Solution:
    # Hashmap Solution
    # TC: O(n) where n = # bricks in wall
    # SC: O(g) where g = # gaps in the wall
    def leastBricks(self, wall: List[List[int]]) -> int:
        gapCount = defaultdict(int)  # gap pos : gap count

        for row in wall:
            total = 0
            # exclude last brick to avoid the gap at the end of the row
            for brick in row[:-1]:
                total += brick
                gapCount[total] += 1

        maxGaps = max(gapCount.values(), default=0)  # handle edge case where gapCount is empty
        
        return len(wall) - maxGaps
