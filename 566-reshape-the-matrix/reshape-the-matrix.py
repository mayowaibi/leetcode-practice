class Solution:
    # TC: O(n*m), SC: O(n*m)
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])

        # if reshape is not valid, return the original matrix
        if r * c != ROWS * COLS:
            return mat
        
        # if r * c is valid, build the new matrix
        output = [[0 for x in range(c)] for x in range(r)]

        # using a temp array to flatten original matrix
        tmp = []

        # add all nums in original matrix to temp array
        for i in range(ROWS):
            for j in range(COLS):
                tmp.append(mat[i][j])
         
        # add nums to output matrix from tmp
        idx = 0     # to keep track of index in tmp
        for i in range(r):
            for j in range(c):
                output[i][j] = tmp[idx]
                idx += 1

        return output