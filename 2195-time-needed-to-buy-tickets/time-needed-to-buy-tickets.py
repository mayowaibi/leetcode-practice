class Solution:
    # Basic Array Traversal - TC: O(n), SC: O(1) 
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0

        for i in range(len(tickets)):
            # 1st Case: Current value comes before k's value
            if i <= k:
                result += min(tickets[i], tickets[k])
            # 2nd Case: Current value comes after k's value
            else:
                result += min(tickets[i], tickets[k] - 1)

        return result