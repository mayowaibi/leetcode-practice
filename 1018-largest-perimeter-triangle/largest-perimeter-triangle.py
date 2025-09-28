class Solution:
    # Greedy + Triangle Inequality Theorem - TC: O(nlogn), SC: O(1)
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)

        for i in range(n-2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]

        return 0