"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    # Sorting Solution - TC: O(nlogn), SC: O(1)
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # sort intervals based on start times
        intervals.sort(key = lambda i : i.start)

        # start at 1 so i-1 can be referenced
        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]

            if i2.start < i1.end:
                return False

        return True
