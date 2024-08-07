class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        numMap = Counter(nums)

        for val in numMap.values():
            if val > 2:
                return False

        return True