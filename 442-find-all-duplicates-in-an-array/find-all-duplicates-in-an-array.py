class Solution:
    # Solution 1: Optimal NeetCode Solution
    # TC - O(n), SC - O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for n in nums:
            # obtain absolute value in case n is negative
            n = abs(n)
            # if number's index is negative, it has been visited before, so it can be added to result
            if nums[n - 1] < 0:
                result.append(n)
            # mark the number's index as visited by negating it
            nums[n - 1] = -nums[n - 1]
                    
        return result

    # Solution 2: Using a Set
    # TC - O(n), SC - O(n)
    def findDuplicates2(self, nums: List[int]) -> List[int]:
        numset = set()
        result = list()

        for n in nums:
            if n in numset:
                result.append(n)
            numset.add(n)
                    
        return result

    # Solution 3: Two Pointer Brute Force
    # TC - O(n^2), SC - O(1)
    def findDuplicates3(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    result.append(nums[i])

        return result