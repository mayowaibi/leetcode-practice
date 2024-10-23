class Solution:
    # Optimal Brute-Force Solution - TC: O(n^2), SC: O(1) assuming output matrix is excluded
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0 for x in range(n)] for x in range(n)]
        MAX_VAL = n ** 2
        top, left, bottom, right = 0, 0, n, n
        curr = 1

        while top < bottom and left < right:
            # update every i in top row
            for i in range(left, right):
                output[top][i] = curr
                curr += 1
            top += 1

            # update every i in right col
            for i in range(top, bottom):
                output[i][right-1] = curr
                curr += 1
            right -= 1

            if not(top < bottom and left < right):
                break
            
            # update every i in bottom row
            for i in range(right - 1, left - 1, -1):
                output[bottom-1][i] = curr
                curr += 1
            bottom -= 1

            # update every i in left col
            for i in range(bottom - 1, top - 1, -1):
                output[i][left] = curr
                curr += 1
            left += 1
        
        return output               