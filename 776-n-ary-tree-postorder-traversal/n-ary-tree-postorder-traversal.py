"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # Iterative DFS Solution - TC: O(n), SC: O(n)
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children:
                stack.append(child)
        
        return res[::-1]  # Reverse to change output to postorder

    # Recursive DFS Solution - TC: O(n), SC: O(n)
    def postorder1(self, root: 'Node') -> List[int]:
        res = []

        if not root:
            return None
        
        for child in root.children:
            res += self.postorder(child)

        res.append(root.val)
        return res
