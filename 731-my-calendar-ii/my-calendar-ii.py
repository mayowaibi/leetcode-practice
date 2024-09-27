class MyCalendarTwo:

    def __init__(self):
        self.non_overlapping = []
        self.overlapping = []

    # Double Array Solution - TC: O(n), SC: O(n)
    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping:
            if not (end <= s or e <= start):
                return False

        for s, e in self.non_overlapping:
            """ Same cond. as before but now we add overlapping interval to overlapping array
            instead of returning false """
            if end > s and e > start:
                self.overlapping.append((max(start, s), min(end, e)))

        self.non_overlapping.append((start, end))

        return True
        



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)