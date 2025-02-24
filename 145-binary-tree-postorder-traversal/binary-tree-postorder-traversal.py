# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive Solution - TC:O(n), SC: O(n)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res
    
    # Iterative Solution - TC:O(n), SC: O(n)
    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res, stack = [], [root]

        while stack:
            curr = stack.pop()
            res.append(curr.val)    # process root first

            # push left child first then right child second
            # to ensure its root -> right -> left
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        return res[::-1]    # reverse list to get correct postorder