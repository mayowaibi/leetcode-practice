class Solution:
    # Greedy Fixed Sliding Window Solution - TC: O(n), SC: O(1)
    def minOperations(self, nums: List[int]) -> int:
        num_flips = 0

        # iterate over nums excluding last 2 nums
        for i in range(len(nums) - 2):
            # flip 3 consecutive bits as soon as a 0 is found
            if nums[i] == 0:
                for j in range(3):
                    nums[i+j] = 0 if nums[i+j] == 1 else 1
                num_flips += 1

        # check if last 2 bits are 0 to know if it is impossible for given nums
        return num_flips if nums[-1] == 1 and nums[-2] == 1 else -1