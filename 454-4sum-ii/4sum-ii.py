class Solution:
    # Optimal Hashmap Solution - TC: O(n^2). SC: O(n^2)
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        partial_sums = defaultdict(int)

        # calculate all pairs of sums between nums1 and nums2
        # and store their frequencies in hashmap
        for a in nums1:
            for b in nums2:
                partial_sums[a + b] += 1
            
        res = 0
        # for each pair of values in nums3 and nums4, check
        # if the complement of their sum exists in hashmap
        for c in nums3:
            for d in nums4:
                # this works because (a + b) = -(c + d)
                res += partial_sums[-(c + d)]

        return res


    # Brute Force Solution - TC: O(n^4), SC: O(1)
    def fourSumCount2(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                for k in range(len(nums3)):
                    for l in range(len(nums4)):
                        if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
                            res += 1
                        
        return res
