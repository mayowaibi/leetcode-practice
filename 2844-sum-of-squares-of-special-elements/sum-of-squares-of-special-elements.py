class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        result = 0
        length = len(nums)

        for i, n in enumerate(nums):
            j = i + 1
            if length % j == 0:
                result += nums[i] * nums[i]
        
        return result