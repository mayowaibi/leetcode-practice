# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative BFS Solution - TC: O(n), SC: O(n)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = collections.deque([(root, 1)])

        while q:
            node, depth = q.popleft()

            # if it's a leaf node, simply return current depth
            # BFS ensures you find the first leaf node in the tree
            if not node.left and not node.right:
                return depth
            
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

    # Recursive DFS Solution - TC: O(n), SC: O(h)
    def minDepth2(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        
        # If node is a leaf, return depth as 1
        if root.left is None and root.right is None:
            return 1
        
        # If left subtree is null, recur for right subtree
        if root.left is None:
            return self.minDepth(root.right) + 1
        
        # If right subtree is null, recur for left subtree
        if root.right is None:
            return self.minDepth(root.left) + 1 
        
        # If both children exist, get the min depth from both
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1