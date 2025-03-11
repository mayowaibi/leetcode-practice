class Solution:
    # Hashmap + Sliding Window Solution - TC: O(n), SC: O(3) = O(1)
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        freq = defaultdict(int) # stores freq of 'a', 'b' and 'c'

        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1

            # do when there is at least one a, b and c in curr window
            while len(freq) == 3:
                # add all valid substrings starting at l until end of string
                res += (len(s) - r)

                # shrink window from left
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    freq.pop(s[l])
                l += 1

        return res

    # Brute Force Solution - TC: O(n^2), SC: O(1)
    def numberOfSubstrings2(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            freq = {'a' : 0, 'b' : 0, 'c' : 0}
            for j in range(i, len(s)):
                if s[j] in freq:
                    freq[s[j]] += 1

                if freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                    res += 1

        return res