class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numSet = set()
        size = 0
        res = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                curr = grid[i][j]
                if curr not in numSet:
                    numSet.add(curr)
                else:
                    res.append(curr)
                size += 1
        
        for i in range(1, size + 1):
            if i not in numSet:
                res.append(i)

        return res