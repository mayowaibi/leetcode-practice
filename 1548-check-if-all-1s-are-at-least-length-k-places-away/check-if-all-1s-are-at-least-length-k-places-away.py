class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # var to keep track of distance between ones
        dist = 0
        # var to denote the first one
        one_seen = False

        for num in nums:
            if one_seen:
                # if 1 is encountered and dist >= k, reset dist to 0
                if num == 1 and dist >= k:
                    dist = 0
                # if 1 is encountered and dist < k, return false
                elif num == 1 and dist < k:
                    return False
                # if 0 is encountered, dist += 1
                else:
                    dist += 1

            # mark when the first one has been found
            if num == 1:
                one_seen = True
        
        # return true after going through all elements in list
        return True