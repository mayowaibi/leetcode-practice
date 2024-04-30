class Solution:
    # Two-Pointer Solution - TC: O(nums1 + nums2), SC: O(1)
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                # first matching val will be smallest val in both arrays since they are in non-decreasing order
                return nums1[i]

        return -1