class StockSpanner:

    def __init__(self):
        self.stock_stack = []

    def next(self, price: int) -> int:
        count = 1
        idx = len(self.stock_stack) - 1
        while idx >= 0:
            if self.stock_stack[idx][0] <= price:
                count += self.stock_stack[idx][1]
                idx -= self.stock_stack[idx][1]
            else:
                break
        self.stock_stack.append((price, count))
        return count
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)