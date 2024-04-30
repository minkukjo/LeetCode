from heapq import heappush, heappop

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min.append(val if not self.min else min(self.min[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()