class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_val.append(val)
        else:
            self.min_val.append(min(val, self.min_val[-1]))
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_val.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_val[-1]
        
