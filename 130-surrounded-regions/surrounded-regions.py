class Solution:
    # Reverse Thinking (NeetCode) Solution - TC: O(m*n), SC: O(1)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        # DFS to capture unsurrounded regions
        def capture_unsurrounded(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"

            capture_unsurrounded(r + 1, c)
            capture_unsurrounded(r - 1, c)
            capture_unsurrounded(r, c + 1)
            capture_unsurrounded(r, c - 1)

        # 1. Capture unsurrounded regions temporarily (O -> T)
        for row in range(ROWS):
            for col in range(COLS):
                # Capture only Os on the board border
                if (row == 0 or col == 0 or row == ROWS-1 or col == COLS-1) and board[row][col] == "O":
                    capture_unsurrounded(row, col)
        
        for row in range(ROWS):
            for col in range(COLS):
                # 2. Capture surrounded regions (O -> X)
                if board[row][col] == "O":
                    board[row][col] = "X"
                # 3. Uncapture unsurrounded regions (T -> O)
                if board[row][col] == "T":
                    board[row][col] = "O"