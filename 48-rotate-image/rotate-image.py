class Solution:
    # 4-Pointer Solution - TC: O(n^2), SC: O(n)
    def rotate(self, matrix: List[List[int]]) -> None:
        left = top = 0
        right = bottom = len(matrix) - 1

        while left < right and top < bottom:
            # iterate through each layer in the matrix, starting from the outermost
            for i in range(right-left):
                # swap every element in the corners of the curr layer
                # use i as offset to accomodate all nums in layer
                (matrix[top][left+i], matrix[top+i][right], matrix[bottom][right-i], matrix[bottom-i][left]) = (matrix[bottom-i][left], matrix[top][left+i], matrix[top+i][right], matrix[bottom][right-i])
        
            # continue to other layers
            left += 1
            right -= 1
            top += 1
            bottom -= 1
            

    # Linear Algebraic Solution - TC: O(n^2), SC: O(n)
    def rotate2(self, matrix: List[List[int]]) -> None:
        # rotating a matrix 90 deg. clockwise =
        # transposing the matrix then reversing its rows
        
        ROWS = COLS = len(matrix)

        # matrix tranpose
        for row in range(ROWS):
            for col in range(row, COLS):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
            # reverse the row after transpose is done
            matrix[row].reverse()