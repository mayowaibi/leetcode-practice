class MyCalendar:

    def __init__(self):
        self.calendar = []

    # Binary Search Implementation - SC: O(logn), TC: O(n)
    def book(self, start: int, end: int) -> bool:
        left, right = 0, len(self.calendar)

        if right == 0:
            self.calendar.append((start, end))
            return True

        while left < right:
            mid = (right - left) // 2 + left
            if self.calendar[mid][1] <= start:
                left = mid + 1
            else:
                right = mid

        if left == len(self.calendar):
            self.calendar.append((start, end))
            return True
                
        if self.calendar[left][0] >= end:
            self.calendar.insert(left, (start, end))
            return True
            
        return False
        
    # Basic List Traversal - SC: O(n), TC: O(n)
    def book2(self, start: int, end: int) -> bool:

        # Check for overlap with existing events
        for s, e in self.calendar:
            # If the new event overlaps with any existing event, return False
            if start < e and end > s:
                return False

        # If no overlap, add the event
        self.calendar.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)