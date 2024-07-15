class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        widths = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                width = len(str(abs(grid[i][j])))
                if grid[i][j] < 0:
                    width += 1
                widths[j] = max(widths[j], width)
        return widths