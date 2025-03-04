# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive Postorder DFS Traversal - TC: O(n), SC: O(n)
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            res += abs(leftSum - rightSum)

            return node.val + leftSum + rightSum
        
        dfs(root)
        return res