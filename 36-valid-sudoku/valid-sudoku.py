class Solution:
    # Hashset Solution - TC: O(9^2), SC: O(9^2)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initialize a hashset for each of the three rules in problem desc.
        # each set contains all values for the given row/col/sub-box
        row_map = defaultdict(set)  # key = row index
        col_map = defaultdict(set)  # key = col index
        sub_box_map = defaultdict(set)  # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                # skip if empty
                if board[r][c] == '.':
                    continue

                # return false if duplicate val is found
                if (board[r][c] in row_map[r] or 
                board[r][c] in col_map[c] or
                board[r][c] in sub_box_map[(r // 3, c // 3)]):
                    return False
                
                # add curr val to all sets
                row_map[r].add(board[r][c])
                col_map[c].add(board[r][c])
                sub_box_map[(r // 3, c // 3)].add(board[r][c])
        
        # board is valid if no duplicate was found
        return True