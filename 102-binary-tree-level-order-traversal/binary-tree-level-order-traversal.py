# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Basic BFS Algo - TC: O(n), SC: O(n/2) = O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = collections.deque()
        # initialize queue with root node if it exists
        if root:
            q.append(root)

        while q:
            level = []
            
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # after each level, add level array to result
            result.append(level)
                
        return result