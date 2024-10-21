class Solution:
    # TC: O(n*m), SC: O(1)
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # start at idx 1 for row and col so there is
        # no out of bound exception within loop
        for i in range(1, ROWS):
            for j in range(1, COLS):
                # for each element, check if it's not
                # equal to its top-right adjacent neighbor
                if matrix[i-1][j-1] != matrix[i][j]:
                    return False
            
        return True
                    