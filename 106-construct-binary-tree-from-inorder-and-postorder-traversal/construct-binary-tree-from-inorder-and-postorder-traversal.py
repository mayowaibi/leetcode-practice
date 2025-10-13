# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive Solution - TC: O(n^2), SC: O(n)
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        
        # create a root node from the last element in postorder
        root = TreeNode(postorder.pop())
        # get index of the root element from inorder
        # this works because there are no duplicate vals in tree
        root_idx = inorder.index(root.val)

        # recursively build left and right subtrees using inorder sublists
        # right subtree must be built first based on postorder list
        root.right = self.buildTree(inorder[root_idx+1:], postorder)
        root.left = self.buildTree(inorder[:root_idx], postorder)

        return root