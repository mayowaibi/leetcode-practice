class Solution:
    # Sliding Window: O(n) TC, O(n) SC
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        charset = set()
        l = 0

        for r in range(len(s)):
            # if there are duplicates in the range, remove the leftmost character and update the left pointer
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            # if there are no duplicates in the range, add the current character (right pointer) to set
            charset.add(s[r])
            # result is the length of the sliding window
            windowLength = r - l + 1
            result = max(result, windowLength)

        return result