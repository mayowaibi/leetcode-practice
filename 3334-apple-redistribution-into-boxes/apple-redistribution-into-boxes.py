class Solution:
    # Greedy Sorting Solution - TC: O(n+mlogm), SC: O(1)
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        num_apples = sum(apple)

        capacity.sort(reverse=True)
        tot_capacity = 0
        res = 0
        for c in capacity:
            tot_capacity += c
            res += 1
            if tot_capacity >= num_apples:
                return res
        
        return res