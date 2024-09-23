class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes, ones, n = 0, 0, len(nums)

        for num in nums:
            if num == 0:
                zeroes += 1
            elif num == 1:
                ones += 1
        
        for i in range(zeroes):
            nums[i] = 0
        for j in range(zeroes, zeroes + ones):
            nums[j] = 1
        for k in range(zeroes + ones, n):
            nums[k] = 2
        