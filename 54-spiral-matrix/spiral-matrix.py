class Solution:
    # Brute Force Solution - TC: O(n*m), SC: O(1) if output matrix is excluded
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        output = []

        while top < bottom and left < right:
            # get every i in the top row
            for i in range(left, right):
                output.append(matrix[top][i])
            top += 1
        
            # get every i in the right col
            for i in range(top, bottom):
                output.append(matrix[i][right-1])
            right -= 1
            
            # edge case check to ensure the while loop
            # guard hasn't been violated mid-loop
            if not (top < bottom and left < right):
                break

            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                output.append(matrix[bottom-1][i])
            bottom -= 1

            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                output.append(matrix[i][left])
            left += 1

        return output

    # Concise Popping Solution - TC: O(n*m), SC: O(1) if output matrix is excluded
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        while matrix:
            # 1 - add all elements in first row
            # use += instead of append to add elements rather than entire list
            res += matrix.pop(0)
            # 2 - add all the last elements in each row sequentially
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            # 3 - add all elements in bottom row in reverse order
            if matrix:
                res += matrix.pop()[::-1]
            # 4 - add all the first elements in each row in reverse order 
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop(0))

        return res