class Solution:
    # Quicksort-Type Solution - TC: O(n), SC: O(n)
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i1, j1 = 0, len(nums) - 1   # pointers for nums arr
        i2, j2 = 0, len(nums) - 1   # pointers for res arr (marking next available slots in res)
        res = [0] * len(nums)

        # adding elements less than and elements greater than pivot in one pass
        # less than - forwards, greater than - backwards; to maintain stability
        while i1 < len(nums):
            if nums[i1] < pivot:
                res[i2] = nums[i1]
                i2 += 1
            if nums[j1] > pivot:
                res[j2] = nums[j1]
                j2 -= 1
            
            # update nums pointers
            i1, j1 = i1 + 1, j1 - 1

        # adding elements equal to pivot
        while i2 <= j2:
            res[i2] = res[j2] = pivot
            i2, j2 = i2 + 1, j2 - 1
        
        return res

    # Triple Array + Array Traversal Solution - TC: O(n), SC: O(n) 
    def pivotArray2(self, nums: List[int], pivot: int) -> List[int]:
        # allocate arrays based on val relative to pivot
        less, eq, greater = [], [], []

        for n in nums:
            if n < pivot:
                less.append(n)
            elif n > pivot:
                greater.append(n)
            else:
                eq.append(n)
            
        return less + eq + greater