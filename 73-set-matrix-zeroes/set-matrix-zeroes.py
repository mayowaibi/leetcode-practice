class Solution:
    # Optimal First Row + Col Flag Solution - TC: O(n*m), SC: O(1)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # in-place algorithm
        ROWS, COLS = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        
        # mark zeros on the first row and column
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    # mark if zero is in the first row
                    if row == 0:
                        first_row_has_zero = True
                    # mark if zero is in the first column
                    if col == 0:
                        first_col_has_zero = True
                    # use first row and column as markers
                    matrix[row][0] = matrix[0][col] = 0

        # use markers to set zeros in the matrix
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        # set zeros for the first row if needed
        if first_row_has_zero:
            for col in range(COLS):
                matrix[0][col] = 0
        
        # set zeros for the first column if needed
        if first_col_has_zero:
            for row in range(ROWS):
                matrix[row][0] = 0

    # List Flag Solution - TC: O(m*n), SC: O(m+n)
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        # in-place algorithm
        ROWS, COLS = len(matrix), len(matrix[0])
        # using true/false as flags for rows/cols that should be changed
        row_flags = [False for _ in range(ROWS)]
        col_flags = [False for _ in range(COLS)]

        # update flags for each row/col in matrix
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    row_flags[row] = True
                    col_flags[col] = True

        # add 0s where necessary based on flags
        for row in range(ROWS):
            for col in range(COLS):
                if row_flags[row] or col_flags[col]:
                    matrix[row][col] = 0