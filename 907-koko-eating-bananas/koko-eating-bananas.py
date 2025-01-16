class Solution:
    # Binary Search Solution - TC: O(log(max(p)) * len(p)), SC: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        # max(piles) is the max value k can be
        res = max(piles)

        while left <= right:
            k = (left + right) // 2

            # calculate hours for current k
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            # update res if hours <= h and smaller k is found
            # then update r pointer to check smaller values
            if hours <= h:
                res = min(res, k)
                right = k - 1
            # if hours > h then update
            # l pointer to check larger k values
            else:
                left = k + 1
            
        return res

    # Brute Force Solution - TC: O(max(p) * len(p)), SC: O(1)
    def minEatingSpeed2(self, piles: List[int], h: int) -> int:
        k = 1

        while True:
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / k)
            if totalTime <= h:
                return k
            k += 1
        return k