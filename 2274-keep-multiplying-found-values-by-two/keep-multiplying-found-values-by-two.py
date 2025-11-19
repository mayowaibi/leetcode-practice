class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            for n in nums:
                if n == original: original *= 2
        
        return original