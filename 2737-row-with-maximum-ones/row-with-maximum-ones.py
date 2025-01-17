class Solution:
    # Brute Force Solution - TC: O(m*n), SC: O(1)
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [0, 0]

        for i in range(len(mat)):
            rowSum = 0
            for j in range(len(mat[0])):
                rowSum += mat[i][j]
            
            if rowSum > res[1]:
                res[0] = i
                res[1] = rowSum

        return res