class Solution:
    # Hashmap Solution - TC: O(n), SC: O(n)
    def findPairs(self, nums: List[int], k: int) -> int:
        num_map = Counter(nums)
        res = 0

        if k == 0:
            # if k is 0, all unique pairs must have the same value
            for key in num_map:
                if num_map[key] >= 2:
                    res += 1
        else:
            for key in num_map:
                if key + k in num_map:
                    res += 1
        
        return res
 
    # Brute Force Solution - TC: O(n^2), SC: O(n)
    def findPairs2(self, nums: List[int], k: int) -> int:
        numSet = set() # to ensure no duplicates are counted

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    # add both combinations of both eligible nums
                    numSet.add((nums[i], nums[j]))
                    numSet.add((nums[j], nums[i]))
        
        res = len(numSet)
        # divide by 2 if k is not 0 to account for duplicate combinations added
        if k != 0:
            res //= 2

        return res