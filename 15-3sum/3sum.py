class Solution:
    # TC: O(nlogn) + O(n^2) = O(n^2), SC - O(n)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # first sort the array so two sum II can be implemented
        nums.sort()

        for i, n in enumerate(nums):
            # skip positive integers
            if n > 0:
                break
            # skip any value if it is the previous value in nums
            if i > 0 and n == nums[i - 1]:
                continue

            # two sum II implementation
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # if threeSum == 0, add numbers to list
                    result.append([n, nums[l], nums[r]])
                    # update left pointer has to be updated
                    # right pointer will be updated in the loop
                    l += 1
                    # to ensure there are no duplicates with previous left pointers
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return result