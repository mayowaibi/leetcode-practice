class Solution:
    # Recursive DFS Solution - TC: O(m*n), SC: O(m*n)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        # return max area of given coord
        def dfs(r, c) -> int:
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r,c))

            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                # only run dfs on islands
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))

        return res