# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # TC: O(log n), SC: O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # if p and q are greater than root, check right subtree
            if p.val > root.val and q.val > root.val:
                root = root.right
            # if p and q are less than root, check left subtree
            elif p.val < root.val and q.val < root.val:
                root = root.left
            # if both conditions fail, the current node (root) can be
            # returned as it is guaranteed to be the LCA
            else:
                return root