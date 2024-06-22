class Solution:
    # Basic Loop Iteration Solution - TC: O(n), SC: O(n)
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        # Divide array into two parts, then iterate through in one loop
        # using the python zip method
        for i, j in zip(nums[:n], nums[n:]):
            result += [i, j]
        return result