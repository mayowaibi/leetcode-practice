class Solution:
    # Hashmap Solution - TC: O(n), SC: O(n)
    def sumOfUnique(self, nums: List[int]) -> int:
        # Counter Implementation
        numsMap = {}

        for num in nums:
            numsMap[num] = 1 + numsMap.get(num, 0)

        res = 0
        for num in numsMap:
            if numsMap[num] == 1:
                res += num
        
        return res