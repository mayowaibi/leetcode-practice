# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive DFS Postorder Solution - TC: O(n), SC: O(h)
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, parent):
            nonlocal res
            if not node:
                return 0

            # Recursively get left and right univalue paths
            left = dfs(node.left, node)
            right = dfs(node.right, node)

            # Update the global max univalue path
            res = max(res, left + right)

            # If current node continues parent's univalue path
            if parent and node.val == parent.val:
                return max(left, right) + 1
            
            return 0  # Reset if it breaks the univalue path
        
        dfs(root, None)
        return res