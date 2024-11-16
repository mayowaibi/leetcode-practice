class Solution:
    # Set and Transpose Solution - TC: O(n), SC: O(n)
    def checkValid(self, matrix: List[List[int]]) -> bool:
        size = len(matrix)

        # traverse through rows in matrix
        for row in matrix:
            if len(set(row)) != size:
                return False

        # traverse through rows of matrix transposed
        # equivalent to traversing through matrix's columns
        for row in list(zip(*matrix)):
            if len(set(row)) != size:
                return False

        return True