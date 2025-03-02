class Solution:
    # Two Pointer Solution - TC: O(n+m), SC: O(1) excl result
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        ptr1, ptr2 = 0, 0

        # compare elements and fill res in order
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1][0] == nums2[ptr2][0]:
                res.append([nums1[ptr1][0], nums1[ptr1][1] + nums2[ptr2][1]])
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1][0] < nums2[ptr2][0]:
                res.append(nums1[ptr1])
                ptr1 += 1
            else:
                res.append(nums2[ptr2])
                ptr2 += 1

        # add remainder elements if any
        if ptr1 < len(nums1):
            res = res + nums1[ptr1:]
        if ptr2 < len(nums2):
            res = res + nums2[ptr2:]

        return res