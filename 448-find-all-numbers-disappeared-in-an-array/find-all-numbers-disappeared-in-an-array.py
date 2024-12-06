class Solution:
    # Optimal Solution - TC: O(n), SC: O(1) assuming returned list doesn't count
    # Solution works because list is from [1, n] so indices can be mapped to that range
    # 1, 2, 3....n maps to 0, 1, 2....n-1
    # 1 - pass through the array to mark each number that has been seen by negating it.
    # 2 - pass through the array again to collate all the +ve numbers (missing nums)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # mark existing nums
        for num in nums:
            # using abs because num may have already been seen
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])
        
        res = []
        # add all missing nums to res
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i+1)
        
        return res

    # Hashset Solution - TC: O(n), SC: O(n) where n is every num in [1, n]
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        numset = set()

        for i in range(1, len(nums)+1):
            numset.add(i)

        for num in nums:
            if num in numset:
                numset.remove(num)
        
        return list(numset)