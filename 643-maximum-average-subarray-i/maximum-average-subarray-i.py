class Solution:
    # Sliding Window Solution - TC: O(n), SC: O(1)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = currSum = sum(nums[:k])   # initial window sum

        for i in range(k, len(nums)):
            currSum += (nums[i] - nums[i-k])   # add new element and remove first element from curr
            maxSum = max(maxSum, currSum)

        return maxSum/k

    # Brute Force Solution - TC: O(n*k), SC: O(1)
    def findMaxAverage2(self, nums: List[int], k: int) -> float:
        maxSum = sum(nums[:k])

        for i in range(len(nums)-k):
            currSum = nums[i]
            for j in range(i+1, i+k):
                currSum += nums[j]
            maxSum = max(maxSum, currSum)

        return maxSum/k