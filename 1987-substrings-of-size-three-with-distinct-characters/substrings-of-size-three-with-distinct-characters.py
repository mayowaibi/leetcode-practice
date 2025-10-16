class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # base case: len of s < 3
        # substrings of fixed len 3
        # if base case isn't reached:
        # start at the third element and simply compare distinctness of all chars
        if len(s) < 3:
            return 0

        count = 0
        
        for i in range(2, len(s)):
            if s[i-2] != s[i-1] and s[i-2] != s[i] and s[i-1] != s[i]:
                count += 1

        return count

        