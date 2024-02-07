class Solution:
    def isValid(self, s: str) -> bool:
        validChars = {')':'(', '}':'{', ']':'['}
        stack = list()

        for char in s:
            if char in validChars:
                # if the char pairs with the char at the top of the stack and the stack is not empty
                if stack and validChars[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            # add char to stack if it's an opening char
            else:
                stack.append(char)
        return not stack # stack.isEmpty()