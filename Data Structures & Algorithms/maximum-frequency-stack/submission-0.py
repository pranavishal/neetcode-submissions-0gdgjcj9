from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.count_map = defaultdict(list)
        self.max_count = 0  

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.max_count = max(self.max_count, self.freq[val])
        self.count_map[self.freq[val]].append(val)

    def pop(self) -> int:
        pop_val = self.count_map[self.max_count].pop()
        if len(self.count_map[self.max_count]) == 0:
            self.max_count -= 1
        self.freq[pop_val] -= 1
        return pop_val   


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()