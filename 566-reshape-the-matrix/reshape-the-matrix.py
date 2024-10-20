class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        # if reshape is not valid, return the original matrix
        if r * c != ROWS * COLS:
            return mat
        
        # if r * c is valid we simply build the new matrix
        new_mat = []

        # using a row to slowly element into the new matrix
        row = []

        # we know the matrix is always 2d, we can use nested for loop
        for i in range(ROWS):
            for j in range(COLS):
                # here we are getting the numbers in order
                # check if the row is the size of c (column)
                if len(row) >= c:
                    # reset the row
                    new_mat.append(row)
                    row = [mat[i][j]]
                else:
                    row.append(mat[i][j])
        
        # since new reshape r * c should fit exactly, we need to append row once more
        new_mat.append(row)
        return new_mat