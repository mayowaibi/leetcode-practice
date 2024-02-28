class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        length = len(merged)
        # even length
        if length % 2 == 0:
            med1Idx = int(length / 2)
            med2Idx = med1Idx - 1
            return float((merged[med1Idx] + merged[med2Idx]) / 2)
        # odd length
        else:
            medIdx = length // 2
            return float(merged[medIdx]) 
