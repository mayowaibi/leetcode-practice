# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    # Recursive DFS - TC: O(n), SC: O(n)
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # Iterative BFS - TC: O(n), SC: O(n)
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # bfs using a queue, starting from the root until all nodes are visited
        q = deque([root])
        level = 0

        while q:
            # pop every node in the queue then add its (non-null) children
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level

    # Iterative DFS (Preorder) - TC: O(n), SC: O(n)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        maxLevel = 0

        while stack:
            node, depth = stack.pop()

            # for every non-null node, add it's children, whether they are null or not
            if node:
                maxLevel = max(maxLevel, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return maxLevel