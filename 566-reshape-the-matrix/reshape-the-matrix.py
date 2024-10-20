class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """ 
        given a matrix of m * n
        reshape it to r * c
        """
        # if reshape is not valid, we return the original matrix
        # in example 2, it shows that 
        # the reshape r * c is valid only if r * c == m * n
        # right of the start, we can check if r * c == m * n
        if r * c != len(mat) * len(mat[0]):
            return mat
        
        # if r * c is valid we simply build the new matrix
        new_mat = []

        # using a row to slowly element into the new matrix
        row = []

        # we know the matrix is always 2d, we can use nested for loop
        for i in range(len(mat)):
            for j in range(len(mat[0])):
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