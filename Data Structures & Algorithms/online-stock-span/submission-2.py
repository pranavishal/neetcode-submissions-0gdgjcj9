class StockSpanner:

    def __init__(self):
        self.stock_stack = []

    def next(self, price: int) -> int:
        count = 1
        while self.stock_stack and self.stock_stack[-1][0] <= price:
            count += self.stock_stack[-1][1]
            self.stock_stack.pop()
            
        self.stock_stack.append((price, count))
        return count
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)