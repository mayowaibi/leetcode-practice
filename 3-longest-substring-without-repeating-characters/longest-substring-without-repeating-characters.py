class Solution:
    # Sliding Window Solution - TC: O(n), SC: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charset = set()
        
        l = 0
        for r in range(len(s)):
            # if there are duplicates in the range, remove the leftmost character and update the left pointer
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            # if there are no duplicates in the range, add the current character to set
            charset.add(s[r])

            # update res to max window size seen
            res = max(res, r - l + 1)

        return res

    # Brute Force Solution - TC: O(n^2), SC: O(n)
    def lengthOfLongestSubstring2(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
                res = max(res, j - i + 1)
        
        return res