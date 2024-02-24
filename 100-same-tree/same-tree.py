# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both are empty
        if not p and not q:
            return True
        # one is empty or both values are unequal
        if not p or not q or p.val != q.val:
            return False
        # recursive call
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)