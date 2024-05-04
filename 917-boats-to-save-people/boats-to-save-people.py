class Solution:
    # Sorting + Two-Pointer Solution - TC: O(nlogn), SC: O(1)
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        people.sort() # TC: O(nlogn)
        l, r = 0, len(people) - 1

        # TC: O(n)
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
    
            result += 1
            r -= 1

        return result

    # Same solution but less concise
    def numRescueBoats2(self, people: List[int], limit: int) -> int:
        result = 0
        people.sort() # TC: O(nlogn)
        l, r = 0, len(people) - 1

        # TC: O(n)
        while l <= r:
            if people[l] + people[r] > limit:
                # give the person on the r index their own boat
                result += 1
                r -= 1
            else:
                # if combined weight is <= limit
                # let the ppl on the l and r index share a boat
                # if l == r, add a boat and terminate loop
                result += 1
                l += 1
                r -= 1

        return result