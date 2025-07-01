class Solution:
    # TC: O(n), SC: O(n)
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        keyStr = s.replace('-', '').upper()
        res = []   # using list instead of string to prevent string rebuilding with concat
            
        curr = 0
        # traverse through key backwards to add dashes based on k
        for c in keyStr[::-1]:
            if curr == k:
                res.append('-')
                curr = 0
            res.append(c)
            curr += 1

        return ''.join(res[::-1])