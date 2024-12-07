class Solution:
    # Sorting + Hashmap Solution - TC: O(nlogn), SC: O(n)
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        # key : value
        # n   : index in sorted list (for first occurrence of num), also represents num of nums smaller than n
        hashmap = {}

        for i, num in enumerate(sorted_nums):
            # only set num to index if it is the first occurrence
            if num not in hashmap:
                hashmap[num] = i

        res = []
        for num in nums:
            res.append(hashmap[num])

        return res

    # Brute Force Solution - TC: O(n^2), SC: O(n) due to output array
    def smallerNumbersThanCurrent2(self, nums: List[int]) -> List[int]:
        result = []

        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            result.append(count)
        
        return result
