class Solution:
    # TC: O(n), SC: O(1)
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # var to keep track of distance between ones
        # initialize to k to reset after first 1 is seen
        dist = k

        for num in nums:
            # if 1 is encountered and dist < k, return False
            if num == 1:
                if dist < k:
                    return False
                # if not, reset dist to 0
                dist = 0
            # if 0 is encountered, dist += 1
            else:
                dist += 1

        return True