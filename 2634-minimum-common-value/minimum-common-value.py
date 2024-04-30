class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        minimum = -1
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                # if no min val from arrays has been set, replace min with the first matching val
                # if min val has been set from arrays, replace min with min of old min and current val
                minimum = nums1[i] if minimum <= 0 else min(minimum, nums1[i])
                i += 1
                j += 1

        return minimum