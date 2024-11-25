class Solution:
    # Slicing Solution - TC: O(n*m), SC: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1