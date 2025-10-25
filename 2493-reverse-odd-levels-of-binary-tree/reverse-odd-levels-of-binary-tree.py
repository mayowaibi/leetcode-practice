# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS + Two Pointer Solution - TC: O(n), SC: O(n)
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        q = deque([root])
        level_count = 0

        while q:
            level_list = []

            for _ in range(len(q)):
                node = q.popleft()
                level_list.append(node)  # append the actual node so the values can be swapped later
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_count % 2 == 1:
                l, r = 0, len(level_list) - 1
                while l < r:
                    level_list[l].val, level_list[r].val = level_list[r].val, level_list[l].val
                    l += 1
                    r -= 1

            level_count += 1

        return root