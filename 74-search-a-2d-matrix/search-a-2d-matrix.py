class Solution:
    # Binary Search Solution: TC: O(log m * n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # separate binary searches, first on the entire matrix to find
        # the corresponding row, then on the row to find the target
        ROWS, COLS = len(matrix), len(matrix[0])

        # first binary search
        top, bot = 0, ROWS - 1
        while top <= bot:
            midRow = top + ((bot - top) // 2)
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:   # target is in the current midRow
                break
        
        # second binary search
        l, r = 0, COLS - 1
        while l <= r:
            midVal = l + ((r - l) // 2)
            if target > matrix[midRow][midVal]:
                l = midVal + 1
            elif target < matrix[midRow][midVal]:
                r = midVal - 1
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