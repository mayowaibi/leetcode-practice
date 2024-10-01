class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1Counter = Counter(nums1)

        for num in nums2:
            if num in nums1Counter and nums1Counter[num] > 0:
                res.append(num)
                nums1Counter[num] -= 1
            
        return res