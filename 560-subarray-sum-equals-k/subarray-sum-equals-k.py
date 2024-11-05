class Solution:
    # Prefix Sum Solution - TC: O(n), SC: O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, curr_sum = 0, 0
        # init hashmap with {0:1} to handle cases where subarray = k from start
        prefix_sums = {0:1} # curr_sum : frequency

        for n in nums:
            curr_sum += n
            # diff = target sum needed from a prev prefix sum
            # to form a valid subarray ending at the current n
            diff = curr_sum - k

            # add count of diff to res; represents no. of valid subarrays
            # from previous indices to the current index that have sum of k
            res += prefix_sums.get(diff, 0)

            # update count of current prefix sum in the map
            prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)

        return res

    # Brute Force Solution - TC: O(n^2), SC: O(1)
    def subarraySum2(self, nums: List[int], k: int) -> int:
        res = 0

        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum == k:
                    res += 1
        
        return res