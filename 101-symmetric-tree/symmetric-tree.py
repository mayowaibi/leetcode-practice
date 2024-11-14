# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS Solution - TC: O(n), SC: O(h) where h is tree height
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSameTree(root1, root2):
            # both are null, return True
            if not (root1 or root2):
                return True
            # only one null, return False
            if not (root1 and root2):
                return False
            # values unequal, return False
            if root1.val != root2.val:
                return False
            # recurse to child nodes
            return isSameTree(root1.left, root2.right) and isSameTree(root1.right, root2.left)
        
        return(isSameTree(root.left, root.right))