class Solution:
    # TC: O(n), SC: O(1)
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        x = len(timeSeries)

        if x == 1 or not duration:
            return duration
        
        res = 0
        for i in range(x-1):
            # if there is no overlap
            if timeSeries[i] + duration < timeSeries[i+1]:
                res += duration
            # if there is an overlap
            else:
                res += timeSeries[i+1] - timeSeries[i]

        # add duration of the last poison effect
        res += duration

        return res