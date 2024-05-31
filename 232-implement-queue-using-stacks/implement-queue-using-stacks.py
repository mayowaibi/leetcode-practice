class MyQueue:

    def __init__(self):
        self.inputStack = []
        self.outputStack = []

    def push(self, x: int) -> None:
        self.inputStack.append(x)        

    def pop(self) -> int:
        while self.inputStack:
            self.outputStack.append(self.inputStack.pop())
        result = self.outputStack.pop() if self.outputStack else None
        while self.outputStack:
            self.inputStack.append(self.outputStack.pop())
        return result

    def peek(self) -> int:
        return self.inputStack[0]

    def empty(self) -> bool:
        return len(self.inputStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()