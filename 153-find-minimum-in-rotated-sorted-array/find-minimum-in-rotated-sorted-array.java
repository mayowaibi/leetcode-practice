class Solution {
    // Binary Search Solution - TC: O(logn), SC: O(1) 
    public int findMin(int[] nums) {
        int l = 0, r = nums.length - 1;
        int res = Integer.MAX_VALUE;

        while (l <= r) {
            // If array/subarray is already sorted
            if (nums[l] < nums[r]) {
                res = Math.min(res, nums[l]);
                break;
            }

            int mid = l + (r-l) / 2;
            res = Math.min(res, nums[l]);

            if (nums[mid] >= nums[r]) {
                l = mid + 1;  // Search the right side
            } else {
                r = mid; // Search the left side
            }
        }

        return res;
    }
}