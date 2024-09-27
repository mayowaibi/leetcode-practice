class Tree:
    def __init__(self, start, end):
        self.left, self.right = None, None
        self.start, self.end = start, end
    
    def insert(self, start, end):
        curr = self
        while True:
            if start >= curr.end:
                if not curr.right:
                    curr.right = Tree(start, end)
                    return True
                curr = curr.right
            elif end <= curr.start:
                if not curr.left:
                    curr.left = Tree(start, end)
                    return True
                curr = curr.left
            else:
                return False
                
class MyCalendar:

    def __init__(self):
        self.root = None # for solution 1
        self.calendar = [] # for solutions 2 and 3

    # Binary Search Tree Solution - TC: O(logn), SC: O(n)
    def book(self, start: int, end: int) -> bool:
        # If root does not exist, create it and return true
        if not self.root:
            self.root = Tree(start, end)
            return True

        return self.root.insert(start, end)


    # Binary Search Implementation - SC: O(logn), TC: O(n)
    def book1(self, start: int, end: int) -> bool:
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
        
    # Basic List Traversal - TC: O(n), SC: O(n)
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