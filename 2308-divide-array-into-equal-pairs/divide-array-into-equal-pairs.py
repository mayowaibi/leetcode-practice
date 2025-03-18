class Solution:
    # Hashmap Solution - TC: O(n), SC: O(n)
    def divideArray(self, nums: List[int]) -> bool:
        numCount = Counter(nums)

        for count in numCount.values():
            if count % 2 == 1:
                return False
        
        return True