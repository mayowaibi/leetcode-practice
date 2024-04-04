class Solution:
    # Basic String Traversal - TC: O(n), SC: O(1)
    def maxDepth(self, s: str) -> int:
        result = 0
        curr = 0
        
        for c in s:
            if c == '(':
                curr += 1
                
            result = max(result, curr)

            if c == ')':
                curr -= 1

        return result