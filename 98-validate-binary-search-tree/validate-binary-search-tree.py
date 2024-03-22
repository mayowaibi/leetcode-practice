# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # using a recursive helper function to each node's values using boundaries
        def valid(node, leftB, rightB):
            # BASE CASES
            # an empty tree is a valid BST
            if not node:
                return True
            # if value is outside range, tree is automatically an invalid BST
            if not (leftB < node.val < rightB):
                return False

            # RECURSIVE CALLS
            # left child should be less than current node (rightB) and
            # right child should be greater than current node (leftB)
            return valid(node.left, leftB, node.val) and valid(node.right, node.val, rightB)
        
        # initialize boundary for root to be between +ve and -ve infinity
        return valid(root, float("-inf"), float("inf"))