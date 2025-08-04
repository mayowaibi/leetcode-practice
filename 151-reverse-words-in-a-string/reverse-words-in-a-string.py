class Solution:
    # Pythonic Solution - TC: O(n), SC: O(n)
    # O(1) space solution is very contrived
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])