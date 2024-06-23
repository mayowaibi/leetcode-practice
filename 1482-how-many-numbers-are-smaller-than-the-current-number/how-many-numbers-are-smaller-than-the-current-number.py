class Solution:
    # Array Traversal Solution - TC: O(n^2), SC: O(n)
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []

        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            result.append(count)
        
        return result
