class MyCalendar:

    def __init__(self):
        # Initialize an empty list to store the events
        self.events = []
        
    # Basic List Traversal - SC: O(n), TC: O(n)
    def book(self, start: int, end: int) -> bool:
        # Check for overlap with existing events
        for s, e in self.events:
            # If the new event overlaps with any existing event
            if not (end <= s or start >= e):  # No overlap condition: (new_end <= old_start) or (new_start >= old_end)
                return False
        # If no overlap, add the event
        self.events.append((start, end))
        return True

    # Binary Search Implementation - SC: O(logn), TC: O(n)
    def book1(self, start: int, end: int) -> bool:
        right = len(self.calendar)
        if right == 0:
            self.calendar.append((start, end))
            return True

        left = 0
        while left < right:
            mid = int(left + (right - left)/2)
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

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)