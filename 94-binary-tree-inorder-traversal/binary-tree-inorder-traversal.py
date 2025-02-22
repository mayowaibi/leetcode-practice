# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative Solution - TC: O(n), SC:O(n)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        curr = root

        while curr or stack:
            while curr: # traverse left subtree
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()  # process current node
            res.append(curr.val)
            curr = curr.right   # move to right subtree

        return res

    # Recursive Solution - TC: O(n), SC:O(n)
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res