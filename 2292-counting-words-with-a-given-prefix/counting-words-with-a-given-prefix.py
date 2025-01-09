class Solution:
    # TC: O(N), SC: O(1)
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0

        for word in words:
            if len(pref) <= len(word) and word[:len(pref)] == pref:
                res += 1

        return res