class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapTracker = {}
        for i in range(len(nums)):
            if (target-nums[i]) in mapTracker:
                return [i, mapTracker.get(target-nums[i])]
            mapTracker[nums[i]] = i
        return None