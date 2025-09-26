class Solution:
    # Bottom-Up DP - TC: O(n^2), SC: O(1)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second-last row and move upward
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Update each element to be the sum of itself and the min of the two adjacent elements in the row below
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        
        # The top element now contains the minimum path sum
        return triangle[0][0]