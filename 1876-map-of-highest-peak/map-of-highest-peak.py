class Solution:
    # Multi-source BFS Solution - TC: O(m*n), SC: O(m*n)
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        q = deque()
        res = [[-1] * COLS for _ in range(ROWS)]    # -1 = unvisited index

        for r in range(ROWS):
            for c in range(COLS):
                # enqueue all water cells and change index in res to 0
                if isWater[r][c]:
                    q.append((r, c))
                    res[r][c] = 0

        # BFS where the # of sources == # of water cells
        while q:
            r, c = q.popleft()
            height = res[r][c]

            neighbors = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for nr, nc in neighbors:
                # skip if any neighbor is out of bounds or
                # index has already been visited
                if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or res[nr][nc] != -1):
                    continue

                # add neighbors to queue and update their values
                q.append((nr, nc))
                res[nr][nc] = height + 1
            
        return res
        