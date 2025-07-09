class FindSumPairs:

    # SC: O(nums2)
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    # TC: O(1)
    def add(self, index: int, val: int) -> None:
        # decrement count of old value
        # and increment count of new value
        old_val = self.nums2[index]
        self.freq[old_val] -= 1
        self.freq[old_val+val] += 1

        # add new value to corresponding nums2 idx
        self.nums2[index] += val

    # TC: O(nums1) - better since len(nums1) << len(nums2)
    def count(self, tot: int) -> int:
        res = 0

        for val in self.nums1:
            res += self.freq[tot-val]
        
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)