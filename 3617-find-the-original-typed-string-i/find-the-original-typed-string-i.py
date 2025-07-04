class Solution:
    # TC: O(n), SC: O(1)
    # answer is always at least 1 (the original word itself)
    # the total number of duplicates = the extra possible strings
    def possibleStringCount(self, word: str) -> int:
        res = 1

        for i in range(1, len(word)):
            if word[i-1] == word[i]:
                res += 1

        return res