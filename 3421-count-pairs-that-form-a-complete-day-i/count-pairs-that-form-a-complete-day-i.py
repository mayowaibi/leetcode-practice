class Solution:
    # Brute-Force Solution - TC: O(n^2), SC: O(1)
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        res = 0
        
        for i in range(len(hours)):
            for j in range(i+1, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0:
                    res += 1

        return res