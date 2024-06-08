class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        i, j = 0, 0
        g.sort()
        s.sort()

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                result += 1
            j += 1
        
        return result
            