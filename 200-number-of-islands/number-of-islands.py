class Solution:
    # Solution 1 marks visited islands in the grid as water ('1' -> '0')
    # Solution 2 uses a set to keep track of visited islands
    # Both approaches can be used interchangeably regardless of whether DFS/BFS is used

    # Recursive DFS Solution - TC: O(m*n), SC: O(m*n)
    def numIslands2(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # dfs function to mark every visited island as water
        def dfs(r, c):
            # ensuring args are in bounds and are an island
            if r in range(ROWS) and c in range(COLS) and grid[r][c] == '1':
                # mark land as water
                grid[r][c] = '0'
                # recursively check neighbors up, down, left and right
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r, c+1)


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                # if island is found, update count and run dfs
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)

        return res

    # Iterative BFS Solution - TC: O(m*n), SC: O(m*n)
    def numIslands(self, grid: List[List[str]]) -> int:
        # using a set to keep track of visited index pairs in grid
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        # bfs function to keep track of visited islands
        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                # all adjacent directions to check: up, down, left, right
                directions = [[-1,0],[1,0],[0,-1],[0,1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == '1' and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    res += 1
                    bfs(r, c)

        return res