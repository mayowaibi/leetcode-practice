class Solution:
    # Greedy Sliding Window Solution - TC: O(n), SC: O(1)
    # If two adjacent balloons are the same colour
    # Pop the one with less needed time
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        res = 0

        l = 0
        for r in range(1, n):
            # case 1: not the same colour
            if colors[l] != colors[r]:
                l = r
            # case 2: same colours
            else:
                if neededTime[l] <= neededTime[r]:
                    res += neededTime[l]
                    l = r
                else:
                    res += neededTime[r]
            
        return res