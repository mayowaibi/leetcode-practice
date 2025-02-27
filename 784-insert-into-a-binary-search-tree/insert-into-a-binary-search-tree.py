# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive Solution - TC: O(n), SC: O(n) if tree is not balanced
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        
        return root


    # Iterative Solution - TC: O(n) if tree is not balanced, SC: O(1)
    def insertIntoBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        if not root:
            return newNode
        
        curr = root
        while curr:
            if curr.val < val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = newNode
                    break
            elif curr.val > val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = newNode
                    break
         
        return root