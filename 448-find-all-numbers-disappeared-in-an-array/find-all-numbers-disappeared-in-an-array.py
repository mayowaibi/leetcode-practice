class Solution:
    # Hashset Solution - TC: O(n), SC: O(n) where n is every num in [1, n]
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numset = set()

        for i in range(1, len(nums)+1):
            numset.add(i)

        for num in nums:
            if num in numset:
                numset.remove(num)
        
        return list(numset)