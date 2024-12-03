class Solution:
    # Two Pointer Solution - TC: O(n) where n is the no. of chars in s, 
    # SC: O(n+m) where m is the len of spaces (no. of spaces to add)
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        sp_idx = 0

        for i in range(len(s)):
            # add space only if there are spaces to be added and
            # i matches the value of the current space's index
            if sp_idx < len(spaces) and i == spaces[sp_idx]:
                res += " "
                sp_idx += 1

            # add current char from s in every iteration
            res += s[i]

        return res