class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numCounts = Counter(nums)

        nums.sort(key = lambda x : (numCounts[x], -x))

        return nums