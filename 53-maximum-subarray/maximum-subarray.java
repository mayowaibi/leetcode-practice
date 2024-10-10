class Solution {
    // Basic Array Iteration - TC: O(n), SC: O(1)
    public int maxSubArray(int[] nums) {
        int result = nums[0], currSum = 0;

        for (int n : nums) {
            // If currSum becomes negative, discard its value
            if (currSum < 0) currSum = 0;
            
            currSum += n;
            result = Math.max(result, currSum);
        }

        return result;
    }
}