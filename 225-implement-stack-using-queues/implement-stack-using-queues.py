class MyStack:

    # SC: O(n)
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    # TC: O(1)
    def push(self, x: int) -> None:
        self.q1.append(x)

    # TC: O(n)
    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        popped_element = self.q1.popleft()
        
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        
        return popped_element

    # TC: O(n)
    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        top_element = self.q1[0]
        
        self.q2.append(self.q1.popleft())
        
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        
        return top_element

    # TC: O(1)
    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()