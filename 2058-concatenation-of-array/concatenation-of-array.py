class Solution:
    # +/* Solution - TC: O(n), SC: O(1) if output arr doesn't count
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums # or return nums * 2
    
    # Loop Soluton - TC: O(n), SC: O(1)
    def getConcatenation2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (2*n)
        
        for i in range(n):
            res[i] = nums[i]
            res[i + n] = nums[i]
        
        return res