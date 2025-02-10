class Solution:
    # Stack Solution - TC: O(n), SC: O(n)
    def clearDigits(self, s: str) -> str:
        res = []    # stack

        def isDigit(c):
            return ord("0") <= ord(c) <= ord("9")

        for c in s:
            if not isDigit(c):
                res.append(c)
            else:
                res.pop()

        return "".join(res)