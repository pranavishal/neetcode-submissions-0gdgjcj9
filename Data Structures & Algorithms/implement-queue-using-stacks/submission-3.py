class MyQueue:

    def __init__(self):
        self.stackOne = []
        self.stackTwo = []
        

    def push(self, x: int) -> None:
        self.stackOne.append(x)
        

    def pop(self) -> int:
        if len(self.stackTwo) == 0:
            while len(self.stackOne) > 0:
                self.stackTwo.append(self.stackOne.pop())
        return self.stackTwo.pop()
        

    def peek(self) -> int:
        if len(self.stackTwo) == 0:
            while len(self.stackOne) > 0:
                self.stackTwo.append(self.stackOne.pop())
        
        return self.stackTwo[-1]
        

    def empty(self) -> bool:
        return len(self.stackOne) == 0 and len(self.stackTwo) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()