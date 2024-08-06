class Solution:
    # Intuitive Python Solution - TC: O(n*m), SC: O(1)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()

        for num in nums1:
            if num in nums2:
                res.add(num)
        
        return res

    # Brute Force Solution - TC: O(n*m), SC: O(n)
    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for i in nums1:
            for j in nums2:
                if i == j and j not in res:
                    res.append(j)

        return res