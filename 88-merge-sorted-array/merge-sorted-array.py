class Solution:
    # Three Pointer Solution - TC: O(n), SC: O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1   # point at last non-zero element in nums1
        j = n - 1   # point at last element in nums2
        k = m + n - 1   # point at last element in nums1

        # merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # fill nums1 with leftover nums2 elements, if any
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1