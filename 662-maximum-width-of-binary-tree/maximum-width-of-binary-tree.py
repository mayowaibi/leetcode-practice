# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative BFS Solution - TC: O(n), SC: O(m) where m is max # of nodes on any level
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        # for each node, also store its 1-based index (like a heap)
        q = collections.deque([(root, 1)])

        while q:
            # calc max width of current level
            firstNode, firstIdx = q[0]
            lastNode, lastIdx = q[-1]

            res = max(res, lastIdx - firstIdx + 1)

            # add next level's nodes to queue
            for _ in range(len(q)):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, idx*2))
                if node.right:
                    q.append((node.right, idx*2+1))

        return res