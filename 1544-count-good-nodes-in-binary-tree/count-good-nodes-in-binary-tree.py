# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Pre-order DFS Solution - TC: O(n), SC: O(h)
        def dfs(node: TreeNode, currMax: int) -> int:
            if not node: return 0

            # update the good node count if the current
            # node is greater than the current max
            if node.val >= currMax:
                count = 1
            else:
                count = 0
            
            # update the current max if needed then
            # recurse to the node's children
            currMax = max(currMax, node.val)
            count += dfs(node.left, currMax)
            count += dfs(node.right, currMax)
            
            return count
        
        return dfs(root, root.val)            