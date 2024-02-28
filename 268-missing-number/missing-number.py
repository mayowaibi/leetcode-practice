class Solution:
    # Solution 1 - Difference in sums: O(1) SC, O(n) TC
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        
        for i in range(len(nums)):
            result += (i - nums[i])
        return result


    # Solution 2 - XOR: O(1) SC, O(n) TC
    def missingNumber2(self, nums: List[int]) -> int:
        result = 0

        for i in range(0, len(nums)):
            result ^= 1

        for num in nums:
            result ^= num
        return result

    # Solution 3 - Using a set: O(n) SC, O(n) TC
    def missingNumber3(self, nums: List[int]) -> int:
        hashset = set()

        for i in range(len(nums) + 1):
            hashset.add(i)

        for num in nums:
            if num in hashset:
                hashset.remove(num)
        return hashset.pop()