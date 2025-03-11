class Solution:
    # Set + Sliding Window Solution - TC: O(n), SC: O(k)
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum = currSum = 0
        numset = set()

        l = 0
        for r in range(len(nums)):
            # shrink window until no duplicates AND window size < k
            while nums[r] in numset or len(numset) >= k:
                numset.remove(nums[l])
                currSum -= nums[l]
                l += 1
            
            numset.add(nums[r])
            currSum += nums[r]

            # update max only when window size is exactly k
            if len(numset) == k:
                maxSum = max(maxSum, currSum)
        
        return maxSum