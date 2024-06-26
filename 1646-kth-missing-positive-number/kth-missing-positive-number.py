class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0  # no. of missing numbers
        i = 0  # to keep track of the actual numbers missing
        while count != k:
            i += 1
            if i not in arr:
                count += 1
                if count == k:
                    return i