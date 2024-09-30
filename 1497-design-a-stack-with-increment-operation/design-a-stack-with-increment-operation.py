class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.MAX = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.MAX:
            self.stack.insert(0, x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop(0)
        return -1

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) >= k:
            while k > 0:
                self.stack[-k] += val
                k -= 1
        else:
            for i in range(len(self.stack)):
                self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)