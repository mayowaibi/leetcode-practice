class Solution:
    # Hashmap Solution - TC: O(n), SC: O(n) where n <= 26 
    def findPermutationDifference(self, s: str, t: str) -> int:
        charMap = {}
        res = 0
        for i, c in enumerate(s):
            charMap[c] = i

        for i, c in enumerate(t):
            res += abs(i - charMap[c])
        
        return res
        