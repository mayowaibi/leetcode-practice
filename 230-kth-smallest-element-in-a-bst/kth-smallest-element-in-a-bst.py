# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative DFS - TC: O(n), SC: O(h) where h is the tree height
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            # go to the left-most child of the curr sub-tree
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val
            curr = curr.right

    # Recursive In-order Traversal - TC: O(n), SC: O(n)
    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        # In-order dfs traversal to ensure array is ordered
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k-1]