class Solution:
    # Rotate Matrix 4 Times and Compare - TC: O(n^2), SC: O(1)
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # rotate function from LC 189 - Rotate Array
        def rotate(mat) -> None:
            ROWS = COLS = len(mat)
            
            # transpose matrix
            for row in range(ROWS):
                for col in range(row, COLS):
                    mat[row][col], mat[col][row] = mat[col][row], mat[row][col]
                # reverse its rows
                mat[row].reverse()

        # rotate mat and check if it matches target mat
        for i in range(4):
            if mat == target:
                return True
            rotate(mat)
        
        return False
        
                    