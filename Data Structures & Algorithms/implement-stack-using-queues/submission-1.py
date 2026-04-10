from collections import deque
class MyStack:

    def __init__(self):
        self.queueOne = deque([])
        self.queueTwo = deque([])        

    def push(self, x: int) -> None:
        self.queueTwo.append(x)
        while len(self.queueOne) > 0:
            self.queueTwo.append(self.queueOne.popleft())
        self.queueTwo, self.queueOne = self.queueOne, self.queueTwo

    def pop(self) -> int:
        return self.queueOne.popleft()

    def top(self) -> int:
        return self.queueOne[0]

    def empty(self) -> bool:
        return len(self.queueOne) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()