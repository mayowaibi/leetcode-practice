# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Solution
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subroot is null, it will always be a subtree of root
        if not subRoot:
            return True
        # if root is null, subroot cannot be a subtree of it (assuming subtree is not null from prev condition)
        if not root:
            return False
        # if root and subroot are the same tree, return true
        if self.isSameTree(root, subRoot):
            return True
        # recursive call if root and subRoot are both not null but also not the same tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # helper function to check if two trees are the same
    def isSameTree(self, s, t) -> bool:
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        return False