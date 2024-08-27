class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0

        for s in logs:
            if s == "../" and res:
                res -= 1
            elif s != "./" and s != "../":
                res += 1
        
        return res