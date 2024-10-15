class Solution {
    // Two-Pointer Solution - TC: O(n), SC: O(1)
    public long minimumSteps(String s) {
        int l = 0;
        long steps = 0;

        // Focusing on moving the 0s as far to the left as possible
        // Would ensure that the 1s are all on the right
        for (int r = 0; r < s.length(); r++) {
            if (s.charAt(r) == '0') { 
                steps += r-l;
                l++;
            }
        }
        
        return steps;
    }
}