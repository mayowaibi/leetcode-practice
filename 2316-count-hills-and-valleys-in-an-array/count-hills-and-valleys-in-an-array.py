class Solution:
    # TC: O(n), SC: O(n)
    def countHillValley(self, nums: List[int]) -> int:
        numss = [nums[0]] # new list without adjacent repeating nums

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
            numss.append(nums[i])

        res = 0
        # skip first and last elements in numss
        # since they can never form a hill or valley
        for i in range(1, len(numss) - 1):
            if numss[i-1] < numss[i] and numss[i+1] < numss[i]:
                res += 1
            elif numss[i-1] > numss[i] and numss[i+1] > numss[i]:
                res += 1
        
        return res