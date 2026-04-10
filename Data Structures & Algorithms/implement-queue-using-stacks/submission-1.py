class MyQueue:

    def __init__(self):
        self.stackOne = []
        self.stackTwo = []

    def push(self, x: int) -> None:
        self.stackOne.append(x)

    def pop(self) -> int:
        if not self.stackTwo:
            while self.stackOne:
                self.stackTwo.append(self.stackOne.pop())
        return self.stackTwo.pop()

    def peek(self) -> int:
        if not self.stackTwo:
            while self.stackOne:
                self.stackTwo.append(self.stackOne.pop())
        return self.stackTwo[-1]
        

    def empty(self) -> bool:
        return (len(self.stackTwo) + len(self.stackOne)) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()