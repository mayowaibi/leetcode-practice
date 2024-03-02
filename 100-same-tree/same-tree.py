# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case 1: if both are null, return true
        if not p and not q:
            return True
        # base case 2: if only one is null, return false
        if not p or not q:
            return False
        # recursive case: if both are not null, check root values then check left and right subtrees
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)