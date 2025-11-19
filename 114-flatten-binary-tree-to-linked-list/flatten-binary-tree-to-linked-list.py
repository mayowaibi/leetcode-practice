# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursive DFS Pre-Order Traversal: Root, Left, Right
    # TC: O(n), SC: O(n)
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 1. traverse through entire tree using a dfs pre-order traversal
        # 2. store each node in a list
        # [1, 2, 3, 4, 5, 6]
        # 3. create a new tree with root as first node in list, 
        # root = [1]
        # 4. makes each subseq. element in list a right child of each node in the new tree

        elements = []
        def dfs(node):
            if not node:
                return
            
            elements.append(node)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        curr = root
        for i in range(len(elements)-1):
            curr.left = None
            curr.right = elements[i+1]
            curr = curr.right