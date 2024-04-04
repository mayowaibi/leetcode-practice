class Solution:
    # Basic String Traversal - TC: O(n), SC: O(1)
    def largestOddNumber(self, num: str) -> str:
        # Iterate through num string in reverse, starting from last index and ending at 0, with steps of -1
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[0:i+1]
        return ""