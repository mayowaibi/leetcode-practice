class Solution {
    // Basic Matrix Traversal - TC: O(n*m), O(n*m) 
    public int[][] transpose(int[][] matrix) {
        int ROWS = matrix.length, COLS = matrix[0].length;
        int[][] res = new int[COLS][ROWS];

        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                res[j][i] = matrix[i][j];
            }
        }
        return res;
    }
}