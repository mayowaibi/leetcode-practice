class Solution:
    def isValid(self, s: str) -> bool:
        map = {'}': '{', ')': '(', ']': '['} # opening bracket : closing bracket
        stack = []

        for c in s:
            if c in map:
                if len(stack) != 0 and map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack # return stack.isEmpty()