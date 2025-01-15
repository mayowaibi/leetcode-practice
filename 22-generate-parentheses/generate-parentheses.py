class Solution:
    # Backtracking Stack Solution - TC and SC are based on the formula for combinations stored in res
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        # Recursive backtracking function to get all possible combinations
        def backtrack(openCount, closeCount):
            # base case is when openCount and closeCount = n
            if openCount == closeCount == n:
                # add all parentheses in stack to res as one string
                res.append("".join(stack))
                return
            
            # only add open parentheses if openCount < n
            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closeCount)
                stack.pop()
            
            # only add closing parentheses if closedCount < openCount
            if closeCount < openCount:
                stack.append(")")
                backtrack(openCount, closeCount + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res