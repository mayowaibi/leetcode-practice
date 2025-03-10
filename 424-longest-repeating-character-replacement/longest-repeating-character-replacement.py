class Solution:
    # Hashmap + Sliding Window Solution - TC: O(2n) = O(n), SC: O(26) = O(1)
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = collections.defaultdict(int)
        res = 0

        l = 0
        for r in range(len(s)):
            charCount[s[r]] += 1

            # Num of Replacements = Curr window size - Max char count in curr window
            # Shrink window if num of replacements needed exceeds k
            if (r - l + 1) - max(charCount.values()) > k:
                charCount[s[l]] -= 1
                l += 1

            # update max length of valid window
            res = max(res, r - l + 1)
        
        return res

    # Brute Force Solution - TC: O(n^2), SC: O(1)
    def characterReplacement2(self, s: str, k: int) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            replacements = 0
            for j in range(i, n):
                # Count the number of chars that differ from char i
                if s[j] != s[i]:
                    replacements += 1
                
                if replacements > k:
                    break  # Stop expanding if num of replacements exceeds k
                
                res = max(res, j - i + 1)  # Update max length
            
        return res
        