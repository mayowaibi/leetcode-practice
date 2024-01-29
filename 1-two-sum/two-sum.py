class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToIndex = dict() # value : index

        for index, num in enumerate(nums):
            diff = target - num
            if diff in valueToIndex:
                return [valueToIndex[diff], index]
            valueToIndex[num] = index