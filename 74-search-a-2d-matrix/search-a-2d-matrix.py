class Solution:
    # Binary Search Solution: TC: O(log m * n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        # separate binary searches, first on the entire matrix to find
        # the corresponding row, then on the row to find the target
        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False
        

    # Binary Search On Each Row Solution - TC: O(m * log n)
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        for i in range(ROWS):
            l, r = 0, COLS - 1
            
            while l <= r:
                mid = (l + r) // 2
                if target < matrix[i][mid]:
                    r = mid - 1
                elif target > matrix[i][mid]:
                    l = mid + 1
                else:
                    return True

        return False

    # Brute Force Solution - TC: O(m * n)
    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == target:
                    return True

        return False