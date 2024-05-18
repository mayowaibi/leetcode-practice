class Solution:
    # Two Pointer Solution - SC: O(n), TC: O(1)
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
            
        while l < r:
            if nums[l] % 2 == 0:
                l += 1
            elif nums[r] % 2 == 1:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        return nums

    # List Solution - SC: O(n), TC: O(n)
    def sortArrayByParity1(self, nums: List[int]) -> List[int]:
        l1, l2 = [], []
    
        for num in nums:
            if num % 2 == 0:
                l1.append(num)
            else:
                l2.append(num)
        
        return l1 + l2