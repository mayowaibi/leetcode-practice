class Solution:
    # Prefix Sum Solution - TC: O(n), SC: O(1)
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n

        # Left pass: Calculate moves needed to bring balls from left to right
        count = 0  # Number of balls seen
        ops = 0  # Operations required
        for i in range(n):
            res[i] += ops
            if boxes[i] == '1':
                count += 1
            ops += count  # Add balls to ops for next move

        # Right pass: Calculate moves needed to bring balls from right to left
        count = ops = 0
        for i in range(n - 1, -1, -1):
            res[i] += ops
            if boxes[i] == '1':
                count += 1
            ops += count  # Add balls to ops for next move
        
        return res
        

    # Brute Force Solution - TC: O(n^2), SC: O(1)
    def minOperations2(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * len(boxes)

        for i in range(n):
            for j in range(n):
                if boxes[j] == '1':
                    res[i] += abs(i-j)

        return res