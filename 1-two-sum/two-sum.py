class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapTracker = {} # key = num, value = index (num: index)
        for index, num in enumerate(nums):
            if (target-num) in mapTracker:
                return [index, mapTracker[target-num]]
            mapTracker[num] = index
        return