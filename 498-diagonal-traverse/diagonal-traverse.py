import collections # for second solution

class Solution:
    # Optimal Solution - TC: O(n*m), SC: O(1)
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat: return []

        ROWS, COLS = len(mat), len(mat[0])
        r = c = 0

        output = []

        for i in range(ROWS * COLS):
            output.append(mat[r][c])
            
            # going up
            if (r + c) % 2 == 0:
                # if in the last col, go to next row
                if c == COLS - 1:
                    r += 1
                # if in the first row, go to next col
                elif r == 0:
                    c += 1
                # all other cases, go diagonally up
                else:
                    r -= 1
                    c += 1
            # going down
            else:
                # if in last row, go to next col
                if r == ROWS - 1:
                    c += 1
                # if in the first col, go to next row
                elif c == 0:
                    r += 1
                # all other cases, go diagonally down
                else:
                    r += 1
                    c -= 1

        return output

    # Default Dict Solution - TC: O(n*m), SC: O(n*m)
    def findDiagonalOrder2(self, mat: List[List[int]]) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])
        hashmap = collections.defaultdict(list)   # sum of indices : values in diagonal
        output = []

        # take adv. of the fact that every value in a diagonal
        # has the same i+j value by using it as key for hashmap
        for i in range(ROWS):
            for j in range(COLS):
                hashmap[i+j].append(mat[i][j])
        
        for key in hashmap:
            # if key is even (going down), reverse list of values
            if key % 2 == 0:
                output += (hashmap[key][::-1])   # use += and not append to add just the values to output
            else:
                output += (hashmap[key])

        return output