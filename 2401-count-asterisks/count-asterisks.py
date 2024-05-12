class Solution:
    # TC: O(n), SC:O(1)
    def countAsterisks(self, s: str) -> int:
        isEven = True
        result = 0

        for c in s:
            if c == '|':
                isEven = not isEven
            if isEven and c == '*':
                result += 1
        
        return result
            