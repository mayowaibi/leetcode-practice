class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        
        while(nums[l]<0 and l<r):
            if nums[l]*(-1) == nums[r]:
                return nums[r]
            if nums[l]*(-1) > nums[r]:
                l += 1
            else:
                r -= 1
        
        return -1
                

    # Using a set - TC: O(n), SC: O(n)
    def findMaxK2(self, nums: List[int]) -> int:
        result = -1

        numset = set(nums)

        for num in numset:
            if num * -1 in numset and num > result:
                result = num

        return result