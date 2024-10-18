class Solution:
    # Kadane's Algorithm - TC: O(n), SC: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for n in nums:
            currSum = max(n, currSum + n)
            maxSum = max(currSum, maxSum)

        return maxSum
    
    # Brute Force Solution - TC: O(n^2), SC: O(1)
    def maxSubArray2(self, nums: List[int]) -> int:
        maxSum = nums[0]

        for i in range(len(nums)):
            currSum = nums[i]
            for j in range(i+1, len(nums)):
                currSum += nums[j]
                maxSum = max(maxSum, currSum)
        
        return maxSum