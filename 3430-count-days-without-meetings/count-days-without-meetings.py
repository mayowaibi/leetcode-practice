class Solution:
    # Sorting Solution - TC: O(nlogn), SC: O(1)
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda d : d[0])

        last_end = 0

        for start, end in meetings:
            interval_size = end - max(last_end + 1, start) + 1
            days -= max(interval_size, 0)   # use max to ensure negative interval sizes aren't added
            last_end = max(last_end, end)

        return days