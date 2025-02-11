class Solution:
    # Pythonic Solution
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)  # replace one occurence of part in s
        return s