class Solution:
    # Sorting Solution - TC: O(nlogn), SC: O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])   # lambda function to sort intervals by start times
        res = [intervals[0]]    # init res with first interval for future reference

        # iterate through all intervals, skipping the first
        for start, end in intervals[1:]:
            # save the end time of the last interval in res for reference
            last_end = res[-1][1]

            # if last and current intervals overlap, update last interval's end time in res
            if last_end >= start:
                res[-1][1] = max(last_end, end)     # use max in case last_end > current end
                
            # if intervals don't overlap, simply add current interval
            else:
                res.append([start, end])
            
        return res
