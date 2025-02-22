# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative Solution
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
            
        return result

    # Recursive Solution
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorder(root, result)
        return result
    
    def inorder(self, node: Optional[TreeNode], result: List[int]) -> None:
        if not node:
            return
        self.inorder(node.left, result)
        result.append(node.val)
        self.inorder(node.right, result)