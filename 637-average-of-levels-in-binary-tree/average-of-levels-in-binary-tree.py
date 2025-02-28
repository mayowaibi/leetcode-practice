# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative BFS Solution - TC: O(n), SC: O(m) where m = max # nodes in any level of tree
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        q = collections.deque([root])
        res = []

        while q:
            levelSum, levelCount = 0, len(q)

            for _ in range(levelCount):
                node = q.popleft()
                levelSum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(levelSum/levelCount)

        return res