class Solution:
    # Linear Search Solution - TC: O(n), SC: O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # if newInterval is entirely before the current interval,
            # simply add it and return new list (cuz everything after will be sorted)
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # if newInterval is entirely after the current interval,
            # curr interval can be added to res (newInterval may still overlap with future intervals)
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # if newInterval overlaps with current interval
            else:
                # set newInterval by merging intervals
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # can't add newInterval to res yet cuz it could still overlap with future intervals

        res.append(newInterval)
        return res

    # Merge Intervals Solution - TC: O(nlogn), SC: O(n)
    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        # refer to LC 57 - Merge Intervals for explanation
        def mergeIntervals(intervals) -> List[List[int]]:
            intervals.sort(key = lambda i : i[0])
            res = [intervals[0]]

            for start, end in intervals[1:]:
                last_end = res[-1][1]
                if last_end >= start:
                    res[-1][1] = max(last_end, end)
                else:
                    res.append([start, end])

            return res

        return mergeIntervals(intervals)                
