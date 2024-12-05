# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive DFS Solution - TC: O(n), SC: O(h) where h is the height of the tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base cases
        if not root or root == p or root == q:
            return root

        # recursive case
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # finding the LCA
        # case 1 - l and r contain p and q respectively, so root is the LCA
        if l and r:
            return root
        # case 2 - return the non-null node between l and r
        else:
            return l or r