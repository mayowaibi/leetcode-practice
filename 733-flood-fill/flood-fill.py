class Solution:
    # Recursive DFS Solution - TC: O(n), SC: O(n)
    # where n = num of cells in grid
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_colour: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_colour = image[sr][sc]
        
        if original_colour == new_colour:
            return image

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != original_colour:
                return

            image[r][c] = new_colour

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image
