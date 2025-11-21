class Solution:
    # Optimal Solution - TC: O(m + n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        # start bottom left of matrix
        i = ROWS-1
        j = 0
        
        # any element right to matrix[i][j] will be greater than it.
        # any element to the top of matrix[i][j] will be less than it.
        # continue searching while i and j are within bounds of matrix
        while i >= 0 and j < COLS:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
                
        return False

    # Brute Force Binary Search Solution - TC: O(m * logn), SC: O(1)
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # binary search on each row of the matrix
        for row in range(ROWS):
            l = 0
            r = COLS - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[row][mid] < target:
                    l = mid + 1
                elif matrix[row][mid] > target:
                    r = mid - 1
                else:
                    return True
        
        return False