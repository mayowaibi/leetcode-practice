# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative Solution - TC: O(n), SC: O(n)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res, stack = [], [root]

        while stack:
            curr = stack.pop()
            res.append(curr.val)    # process root first

            # push right child first then left child second
            # to ensure its root -> left -> right
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return res
     
    # Recursive Solution - TC: O(n), SC: O(n)
    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node: Optional[TreeNode]) -> Optional[List[int]]:
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res