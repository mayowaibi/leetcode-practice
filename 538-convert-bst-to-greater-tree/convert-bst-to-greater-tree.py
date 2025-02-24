# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Reverse Inorder Recursive DFS Traversal - TC: O(n), SC: O(n)
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr_sum = 0

        def dfs(node):
            nonlocal curr_sum

            if not node:
                return

            dfs(node.right)

            original = node.val
            node.val += curr_sum
            curr_sum += original

            dfs(node.left)
        
        dfs(root)
        return root